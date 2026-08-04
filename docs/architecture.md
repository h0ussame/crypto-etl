# Crypto ETL Pipeline

A complete end-to-end ETL (Extract, Transform, Load) pipeline for cryptocurrency market data analysis.

## Overview

This project demonstrates a production-ready data pipeline that extracts cryptocurrency data from the CoinGecko API, processes it through multiple validation and transformation stages, persists it in PostgreSQL, and generates analytics insights visualized in Tableau.

## Pipeline Architecture

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

## Project Components

### 1. **Extract** 
Fetch real-time cryptocurrency data from the CoinGecko API, capturing market prices, volumes, and other key metrics.

### 2. **Save Raw Data**
Store unprocessed JSON responses for data lineage and debugging purposes.

### 3. **Inspect**
Validate data quality, check for missing values, and ensure schema consistency before transformation.

### 4. **Transform**
Clean and restructure data using Python (Pandas):
- Handle missing or malformed records
- Normalize currency values
- Create derived metrics and aggregations

### 5. **Load**
Persist cleaned data into PostgreSQL for reliable, queryable storage and historical tracking.

### 6. **Analytics**
Execute SQL queries to derive insights:
- Market trends analysis
- Price correlations
- Volume patterns
- Performance rankings

### 7. **Visualize**
Build interactive Tableau dashboards to communicate findings to stakeholders.

## Tech Stack

- **API**: CoinGecko
- **Processing**: Python, Pandas
- **Database**: PostgreSQL
- **Analytics**: SQL
- **Visualization**: Tableau

## Key Learnings

- Designing robust ETL pipelines with clear separation of concerns
- Working with APIs and handling JSON data formats
- Data quality assurance and validation techniques
- Relational database design and optimization
- Translating data insights into visual narratives

## How to Use

1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Configure PostgreSQL connection settings
4. Run the extraction script
5. Monitor logs through inspection phase
6. Connect Tableau to PostgreSQL database
7. View analytics dashboards

## Future Enhancements

- Real-time data streaming with scheduled jobs
- Automated alerting on market anomalies
- Machine learning predictions on price movements
- Extended data sources (multiple crypto APIs)
- Performance optimization for large-scale data

---

*A practical demonstration of modern data engineering fundamentals*