import os
import sys
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

print("Starting script...", flush=True)

# Load API key from .env
load_dotenv()
api_key = os.getenv("FRED_API_KEY")
print(f"API Key loaded: {api_key[:8]}...", flush=True)

fred = Fred(api_key=api_key)

# Define healthcare-related series to pull
series = {
    "medical_cpi": "CPIMEDSL",
    "healthcare_employment": "HLTHSCPCHCSA",
    "personal_consumption": "PCEPI",
    "disposable_income": "DSPIC96",
    "unemployment": "UNRATE",
    "retail_sales": "RSAFS"
}

os.makedirs("data", exist_ok=True)
all_data = {}

for name, series_id in series.items():
    print(f"Fetching {name}...", flush=True)
    data = fred.get_series(series_id)
    all_data[name] = data
    print(f"  Got {len(data)} records", flush=True)

df = pd.DataFrame(all_data)
df.index.name = "date"
df.to_csv("data/healthcare_indicators.csv")
print("Done! Saved to data/healthcare_indicators.csv", flush=True)
print(df.tail(), flush=True)
import pandas as pd