# import json
# from pathlib import Path
# from datetime import datetime
# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("COINGECKO_API_KEY")


# def fetch_data() :
#     url = "https://api.coingecko.com/api/v3/coins/markets"

#     headers = {
#     "x-cg-demo-api-key": API_KEY
#     }

#     params = {
#     "vs_currency": "usd",
#     "order": "market_cap_desc",
#     "per_page": 100,
#     "page": 1,
#     "sparkline": "false"
# }
    
#     response = requests.get(url, headers=headers, params=params)
    

#     return response.json()


# def store_raw_data(data):
#     output_dir = Path("data/lake/coingecko")
#     output_dir.mkdir(parents=True, exist_ok=True)
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    
#     output_file = output_dir / f"coingecko_data_{timestamp}.json"
#     with open(output_file, "w") as f:
#         json.dump(data, f, indent=4)
        
#     print(f"Saved to {output_file}")



import json
from pathlib import Path
from datetime import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COINGECKO_API_KEY")


def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    headers = {
        "x-cg-demo-api-key": API_KEY
    }

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()


def store_raw_data(data):
    output_dir = Path("data/lake/coingecko")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = output_dir / f"coingecko_data_{timestamp}.json"

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved raw file: {output_file}")