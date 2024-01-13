# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from scripts import pinata, algo_assets, emails
from algosdk.v2client import algod



app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

@app.route('/api/option1', methods=['POST'])
def handle_option1():
    data = request.get_json()
    choice = data.get('choice')
    print(f'Received Option 1 choice: {choice}')

    # Respond with a message
    return jsonify({'message': f'Received Option 1 choice: {choice}'})


@app.route('/api/create-asset', methods=['POST'])
def create_asset():
    """
    Endpoint to create an asset.

    Request JSON Body:
    {
        "trainee_email": "example@example.com",
        "tutor_public_key": "your_tutor_public_key",
        "tutor_private_key": "your_tutor_private_key"
    }

    Returns:
    {
        "status": "success",
        "message": "Asset created successfully",
        "asset_id": "<created_asset_id>"
    }
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        
        # Extract required fields from the JSON data
        trainee_email = data.get('trainee_email')
        tutor_public_key = data.get('tutor_public_key')
        tutor_private_key = data.get('tutor_private_key')

        # Your existing code for certificate and pinata upload

        # Your existing code for Algorand asset creation
        created_asset_id = asset_manager.create_asset(tutor_private_key, tutor_public_key, url)

        # Your existing code for sending an email
        email.send_email(receiver_email=trainee_email, created_asset_id=created_asset_id)

        # Return success response
        response_data = {
            "status": "success",
            "message": "Asset created successfully",
            "asset_id": created_asset_id
        }
        return jsonify(response_data), 200

    except Exception as e:
        # Return error response in case of an exception
        response_data = {
            "status": "error",
            "message": f"Failed to create asset. Error: {str(e)}"
        }
        return jsonify(response_data), 500


    # Create the asset

if __name__ == '__main__':
    app.run(debug=True)
