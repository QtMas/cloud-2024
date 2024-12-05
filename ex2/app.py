# app.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != f"Bearer {os.environ.get('APP_PASSWORD')}":
        return "Unauthorized", 401
    
    with open('/config/config.txt', 'r') as f:
        message = f.read()
    
    return f"Hello from {os.environ.get('APP_ENV')}! Message: {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
