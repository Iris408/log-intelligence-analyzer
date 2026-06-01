from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.log_service import (
    clear_stored_logs,
    get_error_logs,
    get_log_summary,
    get_stored_logs,
    import_logs_to_database,
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


@router.post("/import")
def import_logs(db: Session = Depends(get_db)):
    return import_logs_to_database(db)


@router.get("/stored")
def stored_logs(db: Session = Depends(get_db)):
    return {"logs": get_stored_logs(db)}

@router.delete("/stored")
def delete_stored_logs(db: Session = Depends(get_db)):
    return clear_stored_logs(db)