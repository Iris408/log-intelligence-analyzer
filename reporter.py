def export_report(report_lines):

    with open("analysis_report.txt", "w") as report:

        for line in report_lines:
            report.write(line + "\n")

print("\nReport exported to analysis_report.txt")
