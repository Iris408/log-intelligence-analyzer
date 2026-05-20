from parser import parse_logs
from reporter import export_report
from analytics import (
    calculate_percentages,
    analyze_error_hours
)
from colorama import Fore, Style, init

init()

report_lines = []


log_data, error_counts = parse_logs("sample_logs/server.log")

total_logs = sum(len(logs) for logs in log_data.values())

if total_logs == 0:
    print("No logs found.")
    exit()


print("\n========== LOG ANALYSIS RESULTS ==========")
print("--------------------")

report_lines.append("Log Analysis Results")
report_lines.append("--------------------")


for level, logs in log_data.items():
   
    if level == "INFO":
        color = Fore.GREEN

    elif level == "WARNING":
        color = Fore.YELLOW

    elif level == "ERROR":
        color = Fore.RED

    else:
        color = Fore.WHITE

    percentage = (len(logs) / total_logs) * 100

    line = f"\n{level}: {len(logs)} ({percentage:.1f}%)"

    print(
        color + 
        f"\n{level}: {len(logs)} ({percentage:.1f}%)"
        + Style.RESET_ALL
    )

    report_lines.append(line)

    for log in logs:
        line = f"- {log}"
        print(line)
        report_lines.append(line)


percentage = calculate_percentages(log_data)

hour_counts = analyze_error_hours(log_data)

print("\n========== REPEATED ERROR ANALYSIS ==========")
print("-----------------------")

report_lines.append("\nRepeated Error Analysis")
report_lines.append("-----------------------")


for error, count in error_counts.items():
    line = f"{error}: {count}"
    print(line)
    report_lines.append(line)


sorted_errors = sorted(
    error_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\n========== TOP ERRORS ==========")
print("----------")

report_lines.append("\nTop Errors")
report_lines.append("----------")


for error, count in sorted_errors:
    line = f"{count}x - {error}"
    print(line)
    report_lines.append(line)


print("\n========== ERRORS BY HOUR ==========")
print("--------------")

report_lines.append("\nErrors By Hour")
report_lines.append("--------------")


for hour, count in sorted(hour_counts.items()):
    line = f"{hour}:00 - {count} errors"
    print(line)
    report_lines.append(line)


export_report(report_lines)
