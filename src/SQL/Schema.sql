CREATE TABLE coins (
    coin_id TEXT PRIMARY KEY,
	symbol TEXT NOT NULL,
	name TEXT NOT NULL
);

CREATE TABLE market_snapshots (
    coin_id TEXT NOT NULL,
	ingestion_timestamp TIMESTAMPTZ NOT NULL,
	last_updated TIMESTAMPTZ NOT NULL,

	current_price DOUBLE PRECISION NOT NULL ,
	market_cap BIGINT NOT NULL,
	market_cap_rank INTEGER NOT NULL,
	fully_diluted_valuation BIGINT NOT NULL,
    market_cap_change_24h DOUBLE PRECISION NOT NULL, 
	market_cap_change_percentage_24h DOUBLE PRECISION NOT NULL,
	
	total_volume DOUBLE PRECISION NOT NULL, 
	high_24h DOUBLE PRECISION NOT NULL, 
	low_24h DOUBLE PRECISION NOT NULL, 
	price_change_24h DOUBLE PRECISION, 
	price_change_percentage_24h DOUBLE PRECISION NOT NULL,

	circulating_supply DOUBLE PRECISION NOT NULL, 
	total_supply DOUBLE PRECISION NOT NULL, 
	max_supply DOUBLE PRECISION , 
	
	ath DOUBLE PRECISION NOT NULL,
	ath_change_percentage DOUBLE PRECISION NOT NULL,
	ath_date TIMESTAMPTZ NOT NULL,

	atl DOUBLE PRECISION NOT NULL,
	atl_change_percentage DOUBLE PRECISION NOT NULL,
	atl_date TIMESTAMPTZ NOT NULL,

	

    PRIMARY KEY (coin_id,ingestion_timestamp),

	CONSTRAINT coin_fk
	FOREIGN KEY (coin_id) REFERENCES coins(coin_id)
     
) 


SELECT * FROM coins