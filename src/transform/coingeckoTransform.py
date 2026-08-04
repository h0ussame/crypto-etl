# import json
# import pandas as pd
# import psycopg

# with open("data/lake/coingecko/coingecko_data_20260730_0309.json", "r") as f:
#     data = json.load(f)

# df = pd.DataFrame(data)

# # df.info()

# # print(df.isna().sum())
# # print(df[df["price_change_24h"].isna()])

# # print(df.isna().sum())


# # print(df["roi"].dropna().iloc[0])
# # print(df.isna().sum())

# df = df.drop(columns=["image", "roi"])

# # print(df[df["price_change_24h"].isna()])
# df = df.rename(columns={"id": "coin_id"})
# df["ingestion_timestamp"] = pd.Timestamp.now(tz="UTC")

# date_columns = [
#     "ath_date",
#     "atl_date",
#     "last_updated"
# ]

# df[date_columns] = df[date_columns].apply(pd.to_datetime)
# # df.info()


# ## Sanity checks for some columns
# # print(df["id"].duplicated().sum())
# # print(df["market_cap_rank"].duplicated().sum())
# # print((df["market_cap"] < 0).sum())
# # print((df["total_volume"] < 0).sum())
# # print((df["high_24h"] < df["low_24h"]).sum())

# # print(df.head())




# conn = psycopg.connect(
#     host="localhost",
#     dbname="crypto_market_db",
#     user="postgres",
#     password="password",
#     port=5432
# )

# cursor = conn.cursor()

# coins_df=df[["coin_id", "symbol", "name"]]
# # print(coins_df.head())

# snapshots_df = df[[
#                 "coin_id", 
#                 "ingestion_timestamp",
#                 "last_updated",
                
#                 "current_price",
#                 "market_cap", 
#                 "market_cap_rank",
#                 "fully_diluted_valuation",
#                 "market_cap_change_24h",
#                 "market_cap_change_percentage_24h",
                
#                 "total_volume",
#                 "high_24h",
#                 "low_24h",
#                 "price_change_24h",
#                 "price_change_percentage_24h",
                
                
#                 "circulating_supply",
#                 "total_supply",
#                 "max_supply", 
                
#                 "ath",
#                 "ath_change_percentage",
#                 "ath_date",
                
#                 "atl",
#                 "atl_change_percentage", 
#                 "atl_date"
                
#                 ] ]


# query1 = """
#      INSERT INTO coins (coin_id, symbol, name)
#      VALUES (%s, %s, %s)
#      ON CONFLICT (coin_id) DO NOTHING
#     """
    
# query2 = """
#     INSERT INTO market_snapshots (
#         coin_id,
#         ingestion_timestamp,
#         last_updated,
#         current_price,
#         market_cap,
#         market_cap_rank,
#         fully_diluted_valuation,
#         market_cap_change_24h,
#         market_cap_change_percentage_24h,
#         total_volume,
#         high_24h,
#         low_24h,
#         price_change_24h,
#         price_change_percentage_24h,
#         circulating_supply,
#         total_supply,
#         max_supply,
#         ath,
#         ath_change_percentage,
#         ath_date,
#         atl,
#         atl_change_percentage,
#         atl_date
#     )
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     ON CONFLICT (coin_id, ingestion_timestamp) DO NOTHING
# """
# cursor.executemany(
# query1, list(coins_df.itertuples(index=False, name=None))
#     )

# # conn.commit()

# # cursor.execute("SELECT * FROM coins LIMIT 5")
# # print(cursor.fetchall())

# cursor.executemany(
#     query2, list(snapshots_df.itertuples(index=False, name=None))
# )

# conn.commit()

# df.info()
# cursor.close()
# conn.close()



import pandas as pd


def transform(data):

    df = pd.DataFrame(data)

    df = df.drop(columns=["image", "roi"])

    df = df.rename(columns={"id": "coin_id"})

    df["ingestion_timestamp"] = pd.Timestamp.now(tz="UTC")

    date_columns = [
        "ath_date",
        "atl_date",
        "last_updated"
    ]

    df[date_columns] = df[date_columns].apply(pd.to_datetime)

    return df