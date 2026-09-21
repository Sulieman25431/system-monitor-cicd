import os
from flask import Flask, jsonify
from flask_cors import CORS
from monitor import get_system_metrics

app = Flask(__name__)
CORS(app)  # Enables GitHub Pages to fetch from Render


@app.route('/api/metrics')
def api_metrics():
    return jsonify(get_system_metrics())


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)