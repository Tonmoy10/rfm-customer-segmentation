from dotenv import load_dotenv

load_dotenv()

import kaggle
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from config import KAGGLE_DATASET,DATA_DIR



if __name__=="__main__":
    os.makedirs(DATA_DIR,exist_ok=True)
    kaggle.api.dataset_download_files(KAGGLE_DATASET,path=DATA_DIR,unzip=True)