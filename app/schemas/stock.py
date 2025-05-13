from pydantic import BaseModel
from typing import List

class OverallStats(BaseModel):
    average_price: float
    max_price: float
    min_price: float

class WeeklyAverage(BaseModel):
    week_label: str
    week_start_date: str
    week_end_date:str
    average_price: float

class StockStatsResponse(BaseModel):
    overall: OverallStats
    weekly_averages: List[WeeklyAverage]
