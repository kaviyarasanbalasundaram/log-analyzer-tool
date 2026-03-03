from collections import defaultdict
from datetime import timedelta
from config.settings import BRUTE_FORCE_THRESHOLD, TIME_WINDOW_SECONDS

def detect_bruteforce(logs):
    attempts = defaultdict(list)

    for log in logs:
        if log["status"] == "401":
            attempts[log["ip"]].append(log["timestamp"])

    alerts = []

    for ip, times in attempts.items():
        times.sort()
        for i in range(len(times)):
            window = [t for t in times if t - times[i] <= timedelta(seconds=TIME_WINDOW_SECONDS)]
            if len(window) >= BRUTE_FORCE_THRESHOLD:
                alerts.append(f"Brute force detected from {ip}")
                break

    return alerts