from datetime import timedelta

from sqlalchemy.orm import Session
from app.models import StockPrice
from sqlalchemy.sql import func

def get_overall_stats(db: Session):
    avg_price = db.query(func.avg(StockPrice.price)).scalar()
    max_price = db.query(func.max(StockPrice.price)).scalar()
    min_price = db.query(func.min(StockPrice.price)).scalar()
    return {
        "average_price": round(avg_price, 2),
        "max_price": max_price,
        "min_price": min_price,
    }

def get_weekly_averages(db: Session):
    results = db.query(
        func.date_trunc('week', StockPrice.date).label("week_start_date"),
        func.avg(StockPrice.price).label("average_price")
    ).group_by("week_start_date").order_by("week_start_date").all()

    return [
        {
            "week_label": f"Week {i + 1}",
            "week_start_date": str(row.week_start_date.date()),
            "week_end_date": str((row.week_start_date + timedelta(days=6)).date()),
            "average_price": round(row.average_price, 2)
        }
        for i, row in enumerate(results)
    ]
