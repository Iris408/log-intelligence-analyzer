from pathlib import Path

LOG_FILE_PATH = Path("sample_logs/server.log")
REPORT_FILE_PATH = Path("analysis_report.txt")

def read_log_file():
    if not LOG_FILE_PATH.exists():
        raise []
    
    with LOG_FILE_PATH.open("r", encoding="utf-8") as log_file:
        return log_file.readlines()
    
def read_analysis_report():
    if not REPORT_FILE_PATH.exists():  
        raise []

    with REPORT_FILE_PATH.open("r", encoding="utf-8") as report_file:
        return report_file.read()

def get_log_summary():
    lines = read_log_file()

    summary = {
        "total_lines": len(lines),
        "info_count": 0,
        "warning_count": 0,
        "error_count": 0,
    }        
    for line in lines:
        if "INFO" in line:
            summary["info_count"] += 1
        elif "WARNING" in line:
            summary["warning_count"] += 1
        elif "ERROR" in line:
            summary["error_count"] += 1
    return summary

def get_error_logs():
    lines = read_log_file()

    errors = []
    for line in lines:
        if "ERROR" in line:
            errors.append(line.strip())
    return errors            