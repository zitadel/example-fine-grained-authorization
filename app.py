from flask import Flask, jsonify
from auth import token_required
from access_control import authorize_access

app = Flask(__name__)

# Define the /write_article route.
@app.route('/write_article', methods=['POST'])
@token_required
def write_article():
    authorization = authorize_access('write_article')
    if authorization is not True:
        return authorization
    # Resource-specific code goes here...
    return jsonify({"message": "Article written successfully!"}), 200


# Define the /edit_article route.
@app.route('/edit_article', methods=['PUT'])
@token_required
def edit_article():
    authorization = authorize_access('edit_article')
    if authorization is not True:
        return authorization    
    # Resource-specific code goes here...
    return jsonify({"message": "Article edited successfully!"}), 200

# Define the /review_article route.
@app.route('/review_articles', methods=['GET'])
@token_required
def review_article():
    authorization = authorize_access('review_article')
    if authorization is not True:
        return authorization
    # Resource-specific code goes here...
    return jsonify({"message": "Article review accessed successfully!"}), 200

# Define the /publish_article route.
@app.route('/publish_article', methods=['POST'])
@token_required
def publish_article():
    authorization = authorize_access('publish_article')
    if authorization is not True:
        return authorization
    # Resource-specific code goes here...
    return jsonify({"message": "Article published successfully!"}), 200

# Add more endpoints as needed...

if __name__ == '__main__':
    app.run(debug=True)
