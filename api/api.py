import time
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/login', methods=['POST'])
def login():
    login_json = request.get_json()

    if not login_json:
        return jsonify({'msg': 'Missing JSON'}), 400

    username = login_json.get('username')
    password = login_json.get('password')
    print(username)
    print(password)

    return jsonify({'username': username}), 200

