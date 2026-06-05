import os
import sys
import pandas as pd
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from config import RFM_DATA_PATH

segmentation = {
    r"^(555|554|545)$":"VIP",
    r"^[45][45].$":"Loyal Customers",
    r"51.$":"New Customers",
    r"^[45][23].$":"Potential Customers",
    r"^[12][45].$":"At Risk",
    r"^(111|112|121)$":"Hibernating"
}
def customer_segment(dat):
    for ptrn,label in segmentation.items():
        if re.fullmatch(ptrn,dat):
            return label
    return "Standard Customer"

def segment_assignment():
    
    df = pd.read_csv(RFM_DATA_PATH)

    df["R"] = pd.qcut(df["Recency"],q=5,labels=[5,4,3,2,1])
    df["F"] = pd.qcut(df["Frequency"].rank(method="first"),q=5,labels=[1,2,3,4,5])
    df["M"] = pd.qcut(df["Monetary"],q=5,labels=[1,2,3,4,5])

    df["rfm_score"] = df[["R","F","M"]].astype(str).agg("".join,axis=1)
    df["customer_segmentation"] = df["rfm_score"].apply(customer_segment)

    df.to_csv(RFM_DATA_PATH,index=False)

if __name__=="__main__":
    segment_assignment()