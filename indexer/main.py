from .solana_rpc import get_block, get_latest_slot
from .pumpfun_parser import is_pumpfun_tx
from db.models import PumpTransaction, SessionLocal

def index_blocks(start_slot, end_slot):
    db = SessionLocal()
    for slot in range(start_slot, end_slot + 1):
        block = get_block(slot)
        if not block:
            continue
        for tx in block.get("transactions", []):
            if is_pumpfun_tx(tx):
                sig = tx["transaction"]["signatures"][0]
                if not db.query(PumpTransaction).filter_by(signature=sig).first():
                    db.add(PumpTransaction(slot=slot, signature=sig, data=tx))
                    db.commit()
    db.close()

if __name__ == "__main__":
    latest = get_latest_slot()
    index_blocks(latest - 10, latest)  # Tail scan
