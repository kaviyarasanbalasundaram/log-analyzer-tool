import pandas as pd

def analyze_traffic(logs):
    df = pd.DataFrame(logs)

    summary = df.groupby("ip").size().reset_index(name="request_count")

    return summary