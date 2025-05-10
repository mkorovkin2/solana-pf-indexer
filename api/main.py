from fastapi import FastAPI
from db.models import PumpTransaction, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/transactions")
def get_transactions():
    db = SessionLocal()
    txs = db.query(PumpTransaction).order_by(PumpTransaction.slot.desc()).limit(100).all()
    db.close()
    return [
        {"slot": tx.slot, "signature": tx.signature, "timestamp": tx.timestamp.isoformat()}
        for tx in txs
    ]
