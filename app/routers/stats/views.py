from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.stock import StockStatsResponse
from app.utils import get_overall_stats, get_weekly_averages

router = APIRouter()


@router.get("/relianceNS-strike-stats", response_model=StockStatsResponse)
def get_stock_stats(db: Session = Depends(get_db)):
    overall = get_overall_stats(db)
    weekly =  get_weekly_averages(db)
    return {
        "overall": overall,
        "weekly_averages": weekly
    }
