import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'status': 'API is running on AWS Lambda',
        'endpoint': '/api/metrics'
    }), 200

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    cpu = round(random.uniform(15.0, 45.0), 1)
    ram = round(random.uniform(35.0, 55.0), 1)
    disk = 28.5

    return jsonify({
        'cpu_usage_pct': cpu,
        'ram_usage_pct': ram,
        'disk_usage_pct': disk,
        'status': 'OK'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)