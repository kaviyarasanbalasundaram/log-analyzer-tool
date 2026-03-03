import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] '
    r'"(?P<method>\S+) (?P<endpoint>\S+) .*?" (?P<status>\d+)'
)

def parse_log(file_path):
    structured_logs = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = LOG_PATTERN.search(line)
            if match:
                data = match.groupdict()
                data["timestamp"] = datetime.strptime(
                    data["timestamp"].split()[0],
                    "%d/%b/%Y:%H:%M:%S"
                )
                structured_logs.append(data)

    return structured_logs