from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, JSON, create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DB_URL

Base = declarative_base()

class PumpTransaction(Base):
    __tablename__ = "pump_transactions"
    id = Column(Integer, primary_key=True)
    slot = Column(Integer)
    signature = Column(String, unique=True)
    data = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
