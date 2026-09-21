# Real-Time System Health & Log Monitoring Tool with CI/CD

A modern, real-time system resource monitor and automated logging dashboard built with Python, Flask, and GitHub Actions CI/CD. This application tracks system hardware performance (CPU, RAM, Disk usage) and visualizes the metrics on an interactive dark-mode dashboard with live graphs.

---

## 🚀 Key Features

- **Live Real-Time Dashboard**: Interactive UI built with Tailwind CSS and Chart.js that updates every 2 seconds without page refreshes.
- **Hardware Metric Tracking**: Utilizes `psutil` to track CPU, RAM, and Disk utilization directly from the host system.
- **Automated Logging**: Background logging mechanism that writes health status and performance data to `system_health.log`.
- **Automated CI/CD Pipeline**: Integrated GitHub Actions workflow (`.github/workflows/main.yml`) that triggers automated tests and validation on every push or pull request.
- **RESTful API Endpoint**: Exposes `/api/metrics` to serve system status as JSON for external integrations.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask, `psutil`
- **Frontend**: HTML5, Tailwind CSS (CDN), Chart.js (CDN), JavaScript (ES6 Fetch API)
- **CI/CD & DevOps**: GitHub Actions, Git
- **Logging**: Python `logging` library

---

## 📁 Repository Structure

```text
system-monitor-cicd/
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions CI/CD pipeline configuration
├── templates/
│   └── index.html          # Dashboard UI with Tailwind CSS & Chart.js
├── app.py                  # Main Flask application & API routes
├── monitor.py              # System resource monitoring & logging utility
├── requirements.txt        # Python dependencies
└── system_health.log       # Output log file for system events
