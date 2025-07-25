from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.core.db import Base

class TronAddressRequestDB(Base):
    __tablename__ = "tron_address_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True, nullable=False)
    balance = Column(Float, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 