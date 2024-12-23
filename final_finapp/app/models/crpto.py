from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from ..core.database import Base

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True, index=True)
    crypto_name = Column(String, nullable=False)
    price_usd = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    class Config:
        orm_mode = True