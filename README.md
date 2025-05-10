## Solana Pump.fun Indexer

Indexes Solana blockchain for Pump.fun related transactions using a direct RPC node connection.

### Setup (Locally)
```bash
pip install -r requirements.txt
cp .env.example .env
python -c 'from db.models import init_db; init_db()'
python indexer/main.py
uvicorn api.main:app --reload
```

* before running this, make sure you've set up your local postgres instance and updated your variables in `.env` with the correct `user:password` combination
* ensure that you've created the database `solana_index` in your postgres instance
	* to do this, you can use `psql` ([how to](https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows))
	* connect to your instance via `psql -U postgres` (as superuser)
	* run `CREATE DATABASE solana_index;`

### Setup (Docker)
```bash
docker-compose up --build
```

### Goals
- Full RPC-based indexing
- Pump.fun-specific filtering
- REST API to access data
