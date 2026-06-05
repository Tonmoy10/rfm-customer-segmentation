import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from config import RAW_DATA_PATH,CLEANED_DATA_PATH

def data_process():
    df=pd.read_csv(RAW_DATA_PATH,encoding="latin1")


    df = df.dropna(subset=["CustomerID"],axis=0)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df = df[(df["Quantity"]>0) & (df["UnitPrice"]>0)]
    
    df["CustomerID"] = df["CustomerID"].astype(int).astype(str)

    df.to_csv(CLEANED_DATA_PATH,index=False)

if __name__=="__main__":
    data_process()