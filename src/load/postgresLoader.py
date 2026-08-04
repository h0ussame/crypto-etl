import psycopg
import os

def load(df):
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    HOST = os.getenv("POSTGRES_HOST")
    DB_NAME = os.getenv("POSTGRES_DB_NAME")
    USER = os.getenv("POSTGRES_USER")
    conn = psycopg.connect(
        host=HOST,
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        port=5432
    )

    cursor = conn.cursor()

    coins_df = df[[
        "coin_id",
        "symbol",
        "name"
    ]]

    snapshots_df = df[[
        "coin_id",
        "ingestion_timestamp",
        "last_updated",
        "current_price",
        "market_cap",
        "market_cap_rank",
        "fully_diluted_valuation",
        "market_cap_change_24h",
        "market_cap_change_percentage_24h",
        "total_volume",
        "high_24h",
        "low_24h",
        "price_change_24h",
        "price_change_percentage_24h",
        "circulating_supply",
        "total_supply",
        "max_supply",
        "ath",
        "ath_change_percentage",
        "ath_date",
        "atl",
        "atl_change_percentage",
        "atl_date"
    ]]

    query1 = """
    INSERT INTO coins (coin_id, symbol, name)
    VALUES (%s, %s, %s)
    ON CONFLICT (coin_id) DO NOTHING
    """

    query2 = """
    INSERT INTO market_snapshots (
        coin_id,
        ingestion_timestamp,
        last_updated,
        current_price,
        market_cap,
        market_cap_rank,
        fully_diluted_valuation,
        market_cap_change_24h,
        market_cap_change_percentage_24h,
        total_volume,
        high_24h,
        low_24h,
        price_change_24h,
        price_change_percentage_24h,
        circulating_supply,
        total_supply,
        max_supply,
        ath,
        ath_change_percentage,
        ath_date,
        atl,
        atl_change_percentage,
        atl_date
    )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s
    )
    ON CONFLICT (coin_id, ingestion_timestamp)
    DO NOTHING
    """

    cursor.executemany(
        query1,
        list(coins_df.itertuples(index=False, name=None))
    )

    cursor.executemany(
        query2,
        list(snapshots_df.itertuples(index=False, name=None))
    )

    conn.commit()

    print(f"Inserted {len(coins_df)} coins (duplicates ignored)")
    print(f"Inserted {len(snapshots_df)} snapshots")

    cursor.close()
    conn.close()