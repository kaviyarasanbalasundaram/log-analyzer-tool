from config.settings import SQLI_PATTERNS, XSS_PATTERNS

def detect_web_attacks(logs):
    alerts = []

    for log in logs:
        endpoint = log["endpoint"]

        for pattern in SQLI_PATTERNS:
            if pattern in endpoint:
                alerts.append(f"SQL Injection attempt from {log['ip']}")

        for pattern in XSS_PATTERNS:
            if pattern in endpoint:
                alerts.append(f"XSS attempt from {log['ip']}")

    return alerts