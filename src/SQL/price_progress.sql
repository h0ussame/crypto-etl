-- A query to extract top 10 winner coins, depending on the growth percentage based on the first and last snapshot

WITH Ranked AS (
    SELECT 
       c.coin_id,
       c.name,
       s.current_price,
       ROW_NUMBER() OVER(PARTITION BY c.coin_id ORDER BY s.ingestion_timestamp ASC) AS oldest_observation_rn,
       ROW_NUMBER() OVER(PARTITION BY c.coin_id ORDER BY s.ingestion_timestamp DESC) AS latest_observation_rn,
       MAX(s.ingestion_timestamp) OVER(PARTITION BY c.coin_id) AS latest_ingestion_timestamp,
       MIN(s.ingestion_timestamp) OVER(PARTITION BY c.coin_id) AS oldest_ingestion_timestamp

    FROM coins as c JOIN market_snapshots as s 
    ON c.coin_id=s.coin_id
),
Oldest_snapshot_per_Coin AS (
    SELECT 
       coin_id,
       name,
       current_price,
       oldest_ingestion_timestamp
    FROM Ranked
    WHERE oldest_observation_rn = 1
),

Latest_snapshot_per_Coin AS (
    SELECT 
       coin_id,
       name,
       current_price,
       latest_ingestion_timestamp
    FROM Ranked
    WHERE latest_observation_rn = 1
)

SELECT LS.coin_id, 
       LS.name,
       LS.current_price AS latest_price,
       OS.current_price AS oldest_price,
       ((LS.current_price - OS.current_price) / OS.current_price) * 100 AS percentage_price_progress,
       ((LS.current_price-OS.current_price)) AS price_progress,
       LS.latest_ingestion_timestamp,
       OS.oldest_ingestion_timestamp
FROM Latest_snapshot_per_Coin AS LS JOIN Oldest_snapshot_per_Coin AS OS 
ON LS.coin_id = OS.coin_id
ORDER BY price_progress DESC
LIMIT 10


