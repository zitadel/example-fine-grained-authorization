import os
import jwt
import requests
from functools import wraps
from flask import request, jsonify, g


ZITADEL_INTROSPECTION_URL = os.getenv('ZITADEL_INTROSPECTION_URL')
API_CLIENT_ID = os.getenv('API_CLIENT_ID')
API_CLIENT_SECRET = os.getenv('API_CLIENT_SECRET')

# This function checks the token introspection and populates the flask.g variable with the user's token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            abort(401) # Return status code 401 for Unauthorized if there's no token
        else:
            token = token.split(' ')[1] # The token is in the format "Bearer <token>", we want to extract the actual token

        # Call the introspection endpoint
        introspection_response = requests.post(
            ZITADEL_INTROSPECTION_URL,
            auth=(API_CLIENT_ID, API_CLIENT_SECRET),
            data={'token': token}
        )

        if not introspection_response.json().get('active', False):
            return jsonify({"message": "Invalid token"}), 403
        
        
        # Decode the token and print it for inspection
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        print(f"\n\n***** Decoded Token: {decoded_token} \n\n******")

        # Add the decoded token to Flask's global context
        g.token = decoded_token
     
        return f(*args, **kwargs)
    return decorated

