from fastapi import APIRouter

from app.services.log_service import (
    get_log_summary,
    get_error_logs,
    read_analysis_report,
)

router = APIRouter(prefix="/logs", tags=["logs"])

@router.get("/summary")
def log_summary():
    return get_log_summary()

@router.get("/errors")
def error_logs():
    return {"errors": get_error_logs()}

@router.get("/report")
def analysis_report():
    return {"report": read_analysis_report()}