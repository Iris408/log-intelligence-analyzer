from collections import Counter

def calculate_percentages(log_data):

    total_logs = sum(
        len(logs)
        for logs in log_data.values()
    )

    percentages = {}

    for level, logs in log_data.items():

        if total_logs == 0:
            percentages[leel] = 0

        else:
            percentages[level] = (
                len(logs) / total_logs
            ) * 100

    return percentages

def analyze_error_hours(log_data):

    hour_counts = Counter()

    for log in log_data["ERROR"]:

        if "[" in log and "]" in log:

            timestamp = log.split("]")[0].replace("[", "")

            hour = timestamp.split(":")[0]

            hour_counts[hour] += 1

        return hour_counts
