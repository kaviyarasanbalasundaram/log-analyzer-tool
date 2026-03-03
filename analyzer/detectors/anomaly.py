from collections import Counter
from datetime import timedelta
from config.settings import TIME_WINDOW_SECONDS

def detect_anomalies(logs):
    alerts = []

    # Count requests per IP
    ip_counts = Counter(log["ip"] for log in logs)

    for ip, count in ip_counts.items():
        if count > 100:
            alerts.append(f"High traffic anomaly detected from {ip} ({count} requests)")

    # Detect too many 500 errors
    error_counts = Counter(
        log["ip"] for log in logs if log["status"].startswith("5")
    )

    for ip, count in error_counts.items():
        if count > 10:
            alerts.append(f"Server error anomaly from {ip} ({count} 5xx errors)")

    return alerts