# Crypto ETL Pipeline 🚀

A complete end-to-end ETL (Extract, Transform, Load) pipeline for cryptocurrency market data analysis. Fetches live crypto data from CoinGecko API, transforms it with Python & Pandas, stores it in PostgreSQL, and visualizes insights with Tableau.

## Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL installed and running
- CoinGecko API key (free tier available)

### Setup (5 minutes)

1. **Clone & Install**
   ```bash
   git clone https://github.com/h0ussame/crypto-etl.git
   cd crypto-etl
   pip install -r requirements.txt
   ```

1. **Clone & Setup Virtual Environment**
```bash
   git clone https://github.com/h0ussame/crypto-etl.git
   cd crypto-etl
   
   # Create virtual environment
   python -m venv .venv
   
   # Activate it
   # On Mac/Linux:
   source .venv/bin/activate
   # On Windows:
   .venv\Scripts\activate
```

2. **Configure Environment**
   Create a `.env` file in the root directory:
   ```
   COINGECKO_API_KEY=your_api_key_here
   POSTGRES_HOST=localhost
   POSTGRES_DB_NAME=crypto_market_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_password
   POSTGRES_PORT=5432
   ```

3. **Setup Database**
   ```bash
   psql -U postgres -d postgres -f src/SQL/Schema.sql
   ```

4. **Run the Pipeline**
   ```bash
   python src/main.py
   ```

   
That's it! The pipeline will:
- Fetch 100 top cryptocurrencies from CoinGecko
- Transform and validate the data
- Store raw JSON and processed data
- Insert into PostgreSQL database

---

## Architecture

```
CoinGecko API
    ↓
Extract raw data
    ↓
Save raw data [JSON]
    ↓
Inspect (Data Validation)
    ↓
Transform (Pandas)
    ↓
Load [PostgreSQL]
    ↓
Analytics (SQL)
    ↓
Visualize (Tableau)
```

### Pipeline Stages

| Stage | What it Does | Tech |
|-------|-------------|------|
| **Extract** | Fetch top 100 cryptocurrencies (price, volume, market cap, etc.) | CoinGecko API, Requests |
| **Store Raw** | Save unprocessed JSON for audit trail & debugging | JSON files |
| **Transform** | Clean data, handle nulls, normalize timestamps | Pandas |
| **Load** | Insert coins & market snapshots with deduplication | PostgreSQL, psycopg |
| **Analytics** | Analyze trends, volatility, price movements | SQL |
| **Visualize** | Create interactive dashboards | Tableau |

---

## Project Structure

```
crypto-etl/
├── src/
│   ├── main.py                    # Pipeline orchestrator
│   ├── extract/
│   │   └── coingecko.py          # Fetch data from API & store raw JSON
│   ├── transform/
│   │   └── coingeckoTransform.py # Clean & normalize data
│   ├── load/
│   │   └── postgresLoader.py     # Insert into PostgreSQL
│   └── SQL/
│       ├── Schema.sql             # Database schema
│       ├── basic_analytics.sql    # Sample queries
│       ├── price_progress.sql     # Top gainers/losers
│       └── volatility.sql         # Volatility analysis
├── data/
│   └── lake/coingecko/           # Raw JSON data (auto-created)
├── docs/
│   └── diagrams/
│       └── CryptoETLdiagram.png  # Pipeline visualization
├── .env                           # Environment variables (not in repo)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Key Analytics Queries

### 1. Top 5 Price Gainers (First to Latest Snapshot)
```sql
-- Finds coins with highest price growth over observation period
SELECT name, latest_price, oldest_price, percentage_price_progress
FROM price_progress_analysis
ORDER BY percentage_price_progress DESC
LIMIT 5
```

### 2. Most Volatile Cryptocurrencies
```sql
-- Measures price volatility (std dev / avg price)
SELECT name, volatility_pct
FROM volatility_analysis
ORDER BY volatility_pct DESC
LIMIT 10
```

### 3. Market Snapshot Comparison
```sql
-- Compares coin metrics across snapshots
SELECT coin_id, name, current_price, market_cap, 
       ingestion_timestamp
FROM market_snapshots
ORDER BY market_cap DESC
```

All queries are in `src/SQL/` for easy reference.

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| **API** | CoinGecko (free tier, no API key required) |
| **Language** | Python 3.8+ |
| **Data Processing** | Pandas |
| **Database** | PostgreSQL 12+ |
| **Database Driver** | psycopg (PostgreSQL adapter for Python) |
| **Analytics** | SQL (window functions, CTEs) |
| **Visualization** | Tableau |
| **Environment** | python-dotenv |

---

## Data Schema

### `coins` Table
Stores unique cryptocurrency information:
```sql
- coin_id (TEXT, Primary Key)
- symbol (TEXT)
- name (TEXT)
```

### `market_snapshots` Table
Time-series data for each coin:
```sql
- coin_id (TEXT, Foreign Key)
- ingestion_timestamp (TIMESTAMPTZ)
- last_updated (TIMESTAMPTZ)
- current_price (DOUBLE PRECISION)
- market_cap (BIGINT)
- market_cap_rank (INTEGER)
- 24h price/volume changes
- All-time high/low with dates
- Supply metrics (circulating, total, max)
```

Primary Key: `(coin_id, ingestion_timestamp)` — ensures one snapshot per coin per collection time.

---

## Running Queries

After data is loaded, connect to PostgreSQL and run analytics:

```bash
psql -U postgres -d crypto_market_db

# View all queries
\i src/SQL/price_progress.sql
\i src/SQL/volatility.sql
\i src/SQL/basic_analytics.sql
```

Or export to CSV for Tableau:
```sql
\COPY (SELECT * FROM market_snapshots) TO 'data/market_snapshots.csv' WITH CSV HEADER;
```

---

## Tableau Dashboard

Connect Tableau to PostgreSQL:
1. New Data Source → PostgreSQL
2. Hostname: `localhost`
3. Database: `crypto_market_db`
4. Tables: `coins`, `market_snapshots`

**Sample Visualizations:**
- Price trends over time
- Top 10 coins by market cap
- Volatility ranking
- 24h price change heatmap
- Volume vs price correlation

---

## What I Learned

✅ **API Integration** — Fetching & handling real-world JSON data  
✅ **Data Pipelines** — Clean separation of extract → transform → load  
✅ **Database Design** — Normalized schema with proper constraints  
✅ **SQL Analytics** — Window functions, CTEs, aggregations  
✅ **Data Quality** — Idempotent inserts, deduplication, validation  
✅ **Python Best Practices** — Environment variables, error handling, modular code  

---

## Future Enhancements

- **Scheduling** — Automate with cron jobs or Airflow DAGs
- **Real-time Streaming** — WebSocket connections for live price updates
- **ML Predictions** — Forecast price movements
- **Alerts** — Notify when coins hit certain thresholds
- **Extended APIs** — Add Binance, Kraken data sources
- **Cloud Deployment** — Move to AWS/GCP with Lambda/Cloud Functions

---

## Troubleshooting

**Problem: "POSTGRES_PASSWORD not found"**
- Solution: Create `.env` file with all required variables

**Problem: "Connection refused" to PostgreSQL**
- Solution: Ensure PostgreSQL is running (`brew services start postgresql` on Mac)

**Problem: "Duplicate key value violates unique constraint"**
- Solution: This is handled by `ON CONFLICT DO NOTHING` — safe to re-run pipeline

---

## Files Overview

- **main.py** — Entry point; runs full ETL pipeline
- **coingecko.py** — Fetches API data & stores raw JSON
- **coingeckoTransform.py** — Cleans data & adds timestamps
- **postgresLoader.py** — Loads dataframe into PostgreSQL
- **Schema.sql** — Creates tables & relationships
- **\*analytics.sql** — Analysis queries for insights

---

## Requirements

See `requirements.txt` for all Python dependencies:
```
pandas
requests
psycopg[binary]
python-dotenv
```

Install with:
```bash
pip install -r requirements.txt
```

---

## License

This project is open source and available for learning & portfolio purposes.

---

## Next Steps

1.  Run the pipeline: `python src/main.py`
2.  Connect to PostgreSQL and explore the data
3.  Build visualizations in Tableau
4.  Share insights on LinkedIn
5.  Extend with scheduling or real-time updates

---

**Built with ❤️ for learning data engineering **