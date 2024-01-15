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
        algod_address = "http://localhost:4001"
        algod_token = "a" * 64
        algod_client = algod.AlgodClient(algod_token, algod_address)
        
        asset_manager = algo_assets.AlgoAssetManager(algod_client)
        url = 'https://ipfs.io/ipfs/QmbCZsNosQwss7BXKmcCzGHZZ7PWdSW43ZxMJt3QYuGmth'

        # Your existing code for Algorand asset creation
        created_asset_id = asset_manager.create_asset(tutor_private_key, tutor_public_key, url)

        # Your existing code for sending an email
        emails.send_email(receiver_email=trainee_email, created_asset_id=created_asset_id)

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
    
def validate_receive_asset_input(data):
    """
    Validate and extract input parameters from the JSON data.

    Parameters:
    - data (dict): JSON data received in the request body.

    Returns:
    - address (int): Sender's address.
    - privatekey (int): Sender's private key.
    - created_asset (int): Index of the asset to opt into.

    Raises:
    - ValueError: If any required parameter is missing or not valid.
    """
    # Validate and extract parameters
    try:
        address = data['address']
        privatekey = data['privatekey']
        created_asset = int(data['created_asset'])
        return address, privatekey, created_asset
    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid or missing parameter: {str(e)}")

# Define a Flask route for the receive_asset functionality
@app.route('/receive_asset', methods=['POST'])
def receive_asset_endpoint():
    """
    Flask endpoint for receiving assets. Expects a JSON payload with the following format:
    {
        "address": int,
        "privatekey": int,
        "created_asset": int
    }

    Returns:
    JSON response with transaction ID and status.

    Example response:
    {
        "txid": "transaction_id",
        "status": "success"
    }
    """
    try:
        # Assuming the data is passed as JSON in the request body
        data = request.get_json()

        # Validate and extract parameters
        address, privatekey, created_asset = validate_receive_asset_input(data)

        algod_address = "http://localhost:4001"
        algod_token = "a" * 64
        algod_client = algod.AlgodClient(algod_token, algod_address)
        
        asset_manager = algo_assets.AlgoAssetManager(algod_client)

        # Call the receive_asset method
        txid = asset_manager.receive_asset(address, privatekey, created_asset)

        # Prepare a response with transaction ID and success status
        response = {'txid': txid, 'status': 'success'}
        return jsonify(response)

    except ValueError as e:
        # Handle validation errors and return an error response with a failure status
        error_response = {'error': str(e), 'status': 'failure'}
        return jsonify(error_response), 400  # HTTP status code 400 for bad request
    

def validate_transfer_asset_input(data):
    """
    Validate and extract input parameters from the JSON data.

    Parameters:
    - data (dict): JSON data received in the request body.

    Returns:
    - private_key (str): Sender's private key.
    - sender (str): Sender's address.
    - receiver (str): Receiver's address.
    - created_asset (int): Index of the asset to transfer.

    Raises:
    - ValueError: If any required parameter is missing or not valid.
    """
    # Validate and extract parameters
    try:
        private_key = str(data['private_key'])
        sender = str(data['sender'])
        receiver = str(data['receiver'])
        created_asset = int(data['created_asset'])
        return private_key, sender, receiver, created_asset
    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid or missing parameter: {str(e)}")

# Define a Flask route for the transfer_asset functionality
@app.route('/transfer_asset', methods=['POST'])
def transfer_asset_endpoint():
    """
    Flask endpoint for transferring assets. Expects a JSON payload with the following format:
    {
        "private_key": str,
        "sender": str,
        "receiver": str,
        "created_asset": int
    }

    Returns:
    JSON response with transaction ID and status.

    Example response:
    {
        "txid": "transaction_id",
        "status": "success"
    }
    """
    try:
        # Assuming the data is passed as JSON in the request body
        data = request.get_json()

        # Validate and extract parameters
        private_key, sender, receiver, created_asset = validate_transfer_asset_input(data)

        algod_address = "http://localhost:4001"
        algod_token = "a" * 64
        algod_client = algod.AlgodClient(algod_token, algod_address)
        
        asset_manager = algo_assets.AlgoAssetManager(algod_client)

        # Call the transfer_asset method
        txid = asset_manager.transfer_asset(private_key, sender, receiver, created_asset)

        # Prepare a response with transaction ID and success status
        response = {'txid': txid, 'status': 'success'}
        return jsonify(response)

    except ValueError as e:
        # Handle validation errors and return an error response with a failure status
        error_response = {'error': str(e), 'status': 'failure'}
        return jsonify(error_response), 400  # HTTP status code 400 for bad request


if __name__ == '__main__':
    app.run(debug=True)
