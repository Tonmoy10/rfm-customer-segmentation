import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from config import CLEANED_DATA_PATH,RFM_DATA_PATH
import pandas as pd

df = pd.read_csv(CLEANED_DATA_PATH)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["TotalPrice"] = df["Quantity"]*df["UnitPrice"]

reference_date = df["InvoiceDate"].max() + pd.Timedelta(hours=24)

rfm = df.groupby("CustomerID").agg({
    "InvoiceDate":"max",
    "InvoiceNo":"nunique",
    "TotalPrice":"sum"})

rfm["InvoiceDate"] = (reference_date - rfm["InvoiceDate"]).dt.days

rfm.rename(columns={"InvoiceDate":"Recency","InvoiceNo":"Frequency","TotalPrice":"Monetary"},inplace=True)

rfm.reset_index(inplace=True)
rfm.to_csv(RFM_DATA_PATH,index=False)