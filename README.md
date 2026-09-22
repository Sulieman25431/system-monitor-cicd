# Real-Time System Monitor & CI/CD Pipeline

A lightweight, serverless real-time system performance monitoring application. Built with a Flask microservice hosted on **AWS Lambda** via **AWS API Gateway**, and a dynamic frontend dashboard deployed using **GitHub Pages** with automated **GitHub Actions CI/CD**.

---

## 🌟 Live Links

* **Live Dashboard (Frontend):** [https://sulieman25431.github.io/system-monitor-cicd/](https://sulieman25431.github.io/system-monitor-cicd/)
* **Live API Endpoint (Backend):** `https://009gvrqhoh.execute-api.ap-south-1.amazonaws.com/dev/api/metrics`

---

## 🏗️ Architecture & Data Flow

+---------------------+        HTTP GET        +------------------------+
|  GitHub Pages       | ---------------------> |  AWS API Gateway       |
|  (HTML5/JS/Chart.js)|                        |  (REST Endpoint)       |
+---------------------+                        +------------------------+
^                                               |
|                                               v
CI/CD Deployment                          +------------------------+
|                                   |  AWS Lambda            |
+---------------------+                        |  (Flask Serverless App)|
|  GitHub Actions     |                        +------------------------+
|  (Automated Build)  |                                    |
+---------------------+                                    v
+------------------------+
|  JSON Metrics Payload  |
|  (CPU %, RAM %, Disk %)|
+------------------------+

1. **Frontend:** Fetches CPU, RAM, and Disk metrics every 2 seconds via asynchronous HTTP requests (`fetch`).
2. **API Gateway:** Routes incoming client requests to the serverless backend function.
3. **AWS Lambda:** Runs the Flask serverless application, calculating real-time system usage and metric variations, returning structured JSON payloads.
4. **CI/CD Pipeline:** GitHub Actions automatically tests code quality (linting) and deploys static site updates straight to GitHub Pages upon every push to the `main` branch.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask, Flask-CORS, Zappa, `psutil`
* **Cloud Infrastructure:** AWS Lambda, AWS API Gateway
* **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6+), Chart.js
* **CI/CD & Hosting:** GitHub Actions, GitHub Pages, Git

---

## 🚀 Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sulieman25431/system-monitor-cicd.git](https://github.com/Sulieman25431/system-monitor-cicd.git)
   cd system-monitor-cicd

2. **Set up virtual environment:**
    ```bash
    python -m venv venv
   ```bash
    source venv/Scripts/activate  # On Windows Git Bash

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run local backend server:**
    ```bash
    python app.py

## ☁️ Deployment (AWS Lambda via Zappa)

1. **To deploy updates to AWS Lambda:**
    ```bash
    # Activate virtual environment
     source venv/Scripts/activate

    ```bash
    # Deploy or update stage
    zappa update dev

##📄 License
This project is open-source and available under the MIT License.

