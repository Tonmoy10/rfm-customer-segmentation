import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from config import KAGGLE_DATASET,DATA_DIR, RAW_FILE_NAME, CUSTOM_FILE_NAME

import kaggle



if __name__=="__main__":
    os.makedirs(DATA_DIR,exist_ok=True)
    kaggle.api.dataset_download_files(KAGGLE_DATASET,path=DATA_DIR,unzip=True)

    old_file_path = os.path.join(DATA_DIR,RAW_FILE_NAME)
    new_file_path = os.path.join(DATA_DIR,CUSTOM_FILE_NAME)

    if os.path.exists(old_file_path):
        os.rename(old_file_path,new_file_path)
