# UK RETAIL CUSTOMER SEGMENTATION USING RFM ANALYSIS

## Executive Summary
This project uses RFM (Recency, Frequency, Monetary) architecture to segment customers of a UK-based retail business with the objective of transitioning from generic marketing approach to a data-driven strategy by identifying loyal customers, VIPS and customers at a risk of leaving.

## Dataset
The data is imported from [E-Commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data), containing realistic customer transaction records of a UK-based online retail company.

## Architecture
- **Language:** Python
- **Data Engineering:** Pandas, NumPy
- **Machine Learning:** (TBD)
- **Data Visualization:** (TBD)
- **Environment:** VS Code, Virtual Environment (.venv)

## Methodology
1. **Data Collection:** Kaggle API
2. **Data Cleaning:** Dropped missing CustomerID, converted InvoiceDate to datetime and removed invalid transactions by filter Quantity and UnitPrice to keep only positive values.
3. **Feature Engineering:** (TBD)
4. **Statistical Scoring:** (TBD)
5. **Customer Segmentation:** (TBD)

## Key Insights
*(To be updated as the project moves forward)*

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