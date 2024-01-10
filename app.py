# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run(debug=True)
