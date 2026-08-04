-- 

SELECT c.name,
       STDDEV_POP(s.current_price) AS std_dev,
      (STDDEV_POP(s.current_price) / AVG(s.current_price) ) * 100 as volatility_pct
FROM coins AS c JOIN market_snapshots as s 
ON c.coin_id = s.coin_id
GROUP BY c.coin_id
ORDER BY volatility_pct DESC
limit 10