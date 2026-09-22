import json
import logging
import urllib.request

logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://wbhlsjf5fa.execute-api.ap-south-1.amazonaws.com/dev/api/metrics"


def get_system_metrics(threshold_cpu=80.0, threshold_ram=85.0):
    try:
        req = urllib.request.urlopen(API_URL, timeout=10)
        data = json.loads(req.read().decode('utf-8'))
        cpu = data.get('cpu_usage_pct', 0)
        ram = data.get('ram_usage_pct', 0)
        disk = data.get('disk_usage_pct', 0)
    except Exception as e:
        logging.error(f"Failed to fetch metrics from AWS Lambda: {e}")
        return {"status": "ERROR", "message": str(e)}

    status = "OK"
    if cpu > threshold_cpu or ram > threshold_ram:
        status = "WARNING"
        logging.warning(f"High Resource Usage! CPU: {cpu}%, RAM: {ram}%")
    else:
        logging.info(f"System Normal. CPU: {cpu}%, RAM: {ram}%")

    return {
        "cpu_usage_pct": cpu,
        "ram_usage_pct": ram,
        "disk_usage_pct": disk,
        "status": status
    }


if __name__ == "__main__":
    print(json.dumps(get_system_metrics(), indent=2))