import base64
import jwt
from flask import g, jsonify

# The access_requirements dictionary represents your access control rules.
access_requirements = {
    'write_article': [{'role': 'journalist', 'experience_level': 'junior'},
                      {'role': 'journalist', 'experience_level': 'intermediate'},
                      {'role': 'journalist', 'experience_level': 'senior'}],
    'edit_article': [{'role': 'editor', 'experience_level': 'junior'},
                     {'role': 'editor', 'experience_level': 'intermediate'},
                     {'role': 'editor', 'experience_level': 'senior'}],
    'review_articles': [{'role': 'journalist', 'experience_level': 'senior'},
                        {'role': 'editor', 'experience_level': 'intermediate'},
                        {'role': 'editor', 'experience_level': 'senior'}],
    'publish_article': [{'role': 'journalist', 'experience_level': 'intermediate'},
                        {'role': 'journalist', 'experience_level': 'senior'},
                        {'role': 'editor', 'experience_level': 'senior'}]
    # Add more endpoints as needed...
}

# This function checks if the user is authorized to access the given endpoint.
def authorize_access(endpoint):
    # We assume that the token has already been decoded in auth.py
    decoded_token = g.token
    
    # Initialize role and experience_level variables
    role = None
    experience_level = None

    for claim, value in decoded_token.items():
        if ':experience_level' in claim:
            role, _ = claim.split(':')
            experience_level = base64.b64decode(value).decode('utf-8')
            break

    # If there's no role in the token, return an error
    if not role:
        return jsonify({"message": "Missing role"}), 403


    # If there's a role in the token but no experience level, default the experience level to 'junior'
    if role and not experience_level:
        experience_level = 'junior'

    # If there's no role or experience level in the token, return an error
    if not role or not experience_level:
        return jsonify({"message": "Missing role or experience level"}), 403

    
    # Get the requirements for the requested endpoint
    endpoint_requirements = access_requirements.get(endpoint)
    
    # If the endpoint is not in the access control list, return an error
    if not endpoint_requirements:
        return jsonify({"message": "Endpoint not found in access control list"}), 403

    # Check if the user's role and experience level meet the requirements for the requested endpoint
    for requirement in endpoint_requirements:
        required_role = requirement['role']
        required_experience_level = requirement['experience_level']

        # Experience level hierarchy
        experience_levels = ['junior', 'intermediate', 'senior']

        if role == required_role and experience_levels.index(experience_level) >= experience_levels.index(required_experience_level):
            return True
    
    #return jsonify({"message": "Access denied"}), 403
    return jsonify({"message": f"Access denied! You are a {experience_level} {role} and therefore cannot access {endpoint}"}), 403
