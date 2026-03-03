import json

def generate_reports(logs, alerts, summary):
    summary.to_csv("output/traffic_summary.csv", index=False)

    with open("output/alerts.json", "w") as f:
        json.dump(alerts, f, indent=4)

    print("Reports generated in output/")