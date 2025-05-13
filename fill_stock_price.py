from app.database import SessionLocal, engine
from app.models import StockPrice, Base
from datetime import date, timedelta
import random

Base.metadata.create_all(bind=engine)

db = SessionLocal()

start_date = date.today() - timedelta(days=59)

for i in range(60):
    day = start_date + timedelta(days=i)
    price = round(random.uniform(2200, 2600), 2)
    if not db.query(StockPrice).filter_by(date=day).first():
        db.add(StockPrice(price=price, date=day))

db.commit()
db.close()
print("Seeded 60 days of stock data.")
