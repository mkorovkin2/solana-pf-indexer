import os
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL", "http://localhost:8899")
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/solana_index")