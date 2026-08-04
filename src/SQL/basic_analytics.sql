SELECT * FROM market_snapshots;
SELECT * FROM coins; 



SELECT MAX(ingestion_timestamp) FROM market_snapshots
SELECT MIN(ingestion_timestamp) FROM market_snapshots




WITH 

  latest_snapshot AS (SELECT c.coin_id,c.name,s.current_price
FROM coins as c JOIN market_snapshots as s 
ON c.coin_id=s.coin_id
WHERE ingestion_timestamp = (SELECT MAX(ingestion_timestamp) FROM market_snapshots)
-- ORDER BY s.current_price DESC
),

first_snapshot AS (
SELECT c.coin_id,c.name,s.current_price
FROM coins as c JOIN market_snapshots as s 
ON c.coin_id=s.coin_id
WHERE ingestion_timestamp = (SELECT MIN(ingestion_timestamp) FROM market_snapshots)
-- ORDER BY s.current_price DESC
)

SELECT ls.name, ((ls.current_price - fs.current_price)
/ fs.current_price) * 100 AS difference 
FROM latest_snapshot AS ls JOIN first_snapshot AS fs ON ls.coin_id=fs.coin_id
ORDER BY difference DESC 
LIMIT 5


SELECT 
       c.coin_id,
       c.name,
       s.current_price,
       s.ingestion_timestamp,
       ROW_NUMBER() OVER(PARTITION BY c.coin_id ORDER BY s.ingestion_timestamp DESC ),
       AVG(s.current_price) OVER(PARTITION BY c.coin_id  ) AS avg_price
FROM coins as c JOIN market_snapshots as s 
ON c.coin_id=s.coin_id
ORDER BY avg_price

