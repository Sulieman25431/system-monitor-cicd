import psutil
import json
import logging

logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_system_metrics(threshold_cpu=80.0, threshold_ram=85.0):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

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