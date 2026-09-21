from flask import Flask, render_template_string, jsonify
from monitor import get_system_metrics

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Health Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; text-align: center; padding: 40px; }
        h1 { margin-bottom: 20px; color: #38bdf8; }
        .card-container { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 30px; }
        .card { background-color: #1e293b; border-radius: 12px; padding: 25px; width: 220px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5); }
        .card h3 { margin-top: 0; color: #94a3b8; font-size: 0.9rem; text-transform: uppercase; }
        .card p { font-size: 2rem; font-weight: bold; margin: 10px 0 0 0; color: #38bdf8; }
        .status-ok { color: #22c55e !important; }
        .status-warning { color: #ef4444 !important; }
        .btn { margin-top: 30px; padding: 12px 24px; background-color: #0284c7; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; }
        .btn:hover { background-color: #0369a1; }
    </style>
</head>
<body>
    <h1>System Health & Log Monitor</h1>
    <div class="card-container">
        <div class="card">
            <h3>CPU Usage</h3>
            <p id="cpu">--%</p>
        </div>
        <div class="card">
            <h3>RAM Usage</h3>
            <p id="ram">--%</p>
        </div>
        <div class="card">
            <h3>Disk Usage</h3>
            <p id="disk">--%</p>
        </div>
        <div class="card">
            <h3>Status</h3>
            <p id="status">Checking...</p>
        </div>
    </div>
    <button class="btn" onclick="fetchMetrics()">Refresh Metrics</button>

    <script>
        async function fetchMetrics() {
            try {
                const res = await fetch('/api/metrics');
                const data = await res.json();
                document.getElementById('cpu').innerText = data.cpu_usage_pct + '%';
                document.getElementById('ram').innerText = data.ram_usage_pct + '%';
                document.getElementById('disk').innerText = data.disk_usage_pct + '%';
                
                const statusEl = document.getElementById('status');
                statusEl.innerText = data.status;
                if(data.status === 'OK') {
                    statusEl.className = 'status-ok';
                } else {
                    statusEl.className = 'status-warning';
                }
            } catch (err) {
                console.error('Error fetching metrics:', err);
            }
        }
        fetchMetrics();
        setInterval(fetchMetrics, 5000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/metrics')
def api_metrics():
    return jsonify(get_system_metrics())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)