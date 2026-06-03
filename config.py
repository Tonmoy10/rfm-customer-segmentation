import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR,"data")

RAW_DATA_PATH = os.path.join(DATA_DIR,"raw_data.csv")
CLEANED_DATA_PATH = os.path.join(DATA_DIR,"cleaned_data.csv")

os.makedirs(DATA_DIR, exist_ok = True)

KAGGLE_DATASET = "carrie1/ecommerce-data"