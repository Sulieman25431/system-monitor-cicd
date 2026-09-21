from flask import Flask, render_template, jsonify
from monitor import get_system_metrics

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/metrics')
def api_metrics():
    return jsonify(get_system_metrics())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)