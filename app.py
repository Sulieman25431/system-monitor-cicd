from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "API is running on AWS Lambda", "endpoint": "/api/metrics"})

@app.route('/api/metrics')
def get_metrics():
    # Return metrics formatted for AWS Lambda deployment
    return jsonify({
        'cpu_usage_pct': 18.5,
        'ram_usage_pct': 42.1,
        'disk_usage_pct': 28.5
    })

if __name__ == '__main__':
    app.run(debug=True)