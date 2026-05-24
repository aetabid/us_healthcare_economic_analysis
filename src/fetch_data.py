import os
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))