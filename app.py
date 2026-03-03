import argparse
import logging

from analyzer.parser import parse_log
from analyzer.detectors.brute_force import detect_bruteforce
from analyzer.detectors.web_attacks import detect_web_attacks
from analyzer.detectors.anomaly import detect_anomalies
from analyzer.analytics import analyze_traffic
from analyzer.report import generate_reports

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="Advanced Log Analyzer Tool")
    parser.add_argument("--file", required=True, help="Path to log file")
    args = parser.parse_args()

    # Parse logs
    logs = parse_log(args.file)

    # Run detections
    brute_alerts = detect_bruteforce(logs)
    web_alerts = detect_web_attacks(logs)
    anomaly_alerts = detect_anomalies(logs)

    # Combine alerts
    alerts = brute_alerts + web_alerts + anomaly_alerts

    # Analyze traffic
    summary = analyze_traffic(logs)

    # Generate reports
    generate_reports(logs, alerts, summary)

    logging.info("Analysis Complete")


if __name__ == "__main__":
    main()