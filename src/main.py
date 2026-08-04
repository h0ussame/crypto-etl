# from extract.coingecko import fetch_data, store_raw_data


# def main():
#     data = fetch_data()
#     store_raw_data(data)


# if __name__ == "__main__":
#     main()


from extract.coingecko import fetch_data, store_raw_data
from transform.coingeckoTransform import transform
from load.postgresLoader import load


def main():

    print("========== CoinGecko Pipeline ==========")

    data = fetch_data()

    store_raw_data(data)

    df = transform(data)

    load(df)

    print("Pipeline completed successfully!")

    print("========================================")


if __name__ == "__main__":
    main()