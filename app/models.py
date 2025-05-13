from sqlalchemy import Column, Integer, Float, Date
from .database import Base

class StockPrice(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    date = Column(Date, nullable=False, unique=True)
