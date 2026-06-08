# UK RETAIL CUSTOMER SEGMENTATION USING RFM ANALYSIS

## Executive Summary
This project uses RFM (Recency, Frequency, Monetary) architecture to segment customers of a UK-based retail business with the objective of transitioning from generic marketing approach to a data-driven strategy by identifying loyal customers, VIPS and customers at a risk of leaving.

## Dataset
The data is imported from [E-Commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data), containing realistic customer transaction records of a UK-based online retail company.

## Architecture
- **Language:** Python
- **Data Engineering:** Pandas, NumPy, Re
- **Machine Learning:** K-Means
- **Data Visualization:** Matplotlib, Seaborn
- **Environment:** VS Code, Virtual Environment (.venv)

## Methodology
1. **Data Collection:** Kaggle API
2. **Data Cleaning:** Dropped missing CustomerID, converted InvoiceDate to datetime and removed invalid transactions by filter Quantity and UnitPrice to keep only positive values.
3. **Feature Engineering:** Calculated baseline RFM metric and utilized regex hard-coded rules to create baseline manual segmentation model.
4. **Data Transformation:** Applied logarithmic scaling to fix the heavy right-skewed data.
5. **Machine Learning Clustering:** Used elbow method to identify the optimal number of clusters (K=4) and used that to apply K-Means to apply data-driven partitioning.

## Key Insights
1. **Human Bias:** The manual segmentation misallocate significant amount of customers to wrong segments due to hard-coded rules, such as allocating hibernating-risk customers as loyal ones base on lifetime volume, that might cost the company to lose more customer.
2. **Hidden Revenue and Risk** The machine learning model K-Means solved this problem of hard-coded threshold values, that uncovered hidden VIP customers and detecting customers at risk of leaving at an early stage.
3. **Marketing Optimization** The company should focus on optimizing their marketing strategies to cut off budget for the mislabelled 1000+ hibernating customers and allocate it on automated campaigns to retain customers at risk of leaving.

## How to run this project locally
1. Clone this repository to your local computer.
2. Create and run the virtual environment:
    ```bash
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # Mac/Linux: source .venv/bin/activate
    ```
3. Install the requirements dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create an .env file in the root directory and put your Kaggle API keys:
    ```bash
    KAGGLE_USERNAME=your_username_here
    KAGGLE_KEY=your_key_here
    ```
5. Run the python files in the specific order:
    ```bash
    python src/data_pipeline.py
    python src/data_processing.py
    python src/data_engine.py
    python src/data_scoring.py
6. Run the exploratory notebooks as per the serial in their filename.