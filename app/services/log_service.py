from pathlib import Path
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.log_model import LogEntry

LOG_FILE_PATH = Path("sample_logs/server.log")
REPORT_FILE_PATH = Path("analysis_report.txt")


def read_log_file():
    if not LOG_FILE_PATH.exists():
        raise FileNotFoundError(f"Log file not found: {LOG_FILE_PATH}")
    
    with LOG_FILE_PATH.open("r", encoding="utf-8") as log_file:
        return log_file.readlines()
    
def read_analysis_report():
    if not REPORT_FILE_PATH.exists():  
        raise FileNotFoundError(f"Report file not found: {REPORT_FILE_PATH}")

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

def get_log_severity(line: str) -> str:
    if "ERROR" in line:
        return "ERROR"
    if "WARNING" in line:
        return "WARNING"
    if "INFO" in line:
        return "INFO"
    return "UNKNOWN"

def import_logs_to_database(db: Session):
    lines = read_log_file()

    imported_count = 0

    for line in lines:
        clean_line = line.strip()

        if not clean_line:
            continue

        severity = get_log_severity(clean_line)
        
        log_entry = LogEntry(timestamp=None, severity=severity, message=clean_line)

        db.add(log_entry)
        imported_count += 1

    db.commit()

    return {
        "message": "Logs imported successfully",
        "imported_count": imported_count,
    }    

def get_stored_logs(db: Session):
    from app.models.log_model import LogEntry

    logs = db.query(LogEntry).order_by(LogEntry.created_at.desc()).all()
    results = []

    for log in logs:
        results.append({
            "id": log.id,
            "timestamp": log.timestamp,
            "severity": log.severity,
            "message": log.message,
            "created_at": log.created_at})
        
    return results

def clear_stored_logs(db: Session):
    deleted_count = db.query(LogEntry).delete()

    db.commit()

    return {
        "message": "Stored logs cleared successfully",
        "deleted_count": deleted_count,
    }

def get_latest_log_entries(limit: int = 5):
    lines = read_log_file()

    latest_lines = lines[-limit:]
    results = []

    for line in latest_lines:
        clean_line = line.strip()

        if not clean_line:
            continue

        results.append({
            "severity": get_log_severity(clean_line),
            "message": clean_line,
        })

    return { "latest_logs": results, "total_returned": len(results) }