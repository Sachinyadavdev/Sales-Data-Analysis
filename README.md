# Sales Data Analysis Portfolio Project

## Project Overview
This is a beginner-friendly Python data analysis project designed for a Data Analyst/SDE preparation portfolio. The project demonstrates the end-to-end process of data generation, cleaning, exploratory data analysis (EDA), visualization, and SQL querying.

## Project Objectives
- Generate a synthetic, realistic sales dataset with intentional data quality issues.
- Clean and preprocess the dataset using Pandas.
- Perform exploratory data analysis to extract key business metrics.
- Create meaningful visualizations using Matplotlib and Seaborn.
- Execute SQL queries to analyze the data using SQLite.
- Document business insights and recommendations.

## Technologies Used
- **Language:** Python 3
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Database:** SQLite (via Python's `sqlite3` module)
- **Environment:** Jupyter Notebook

## Folder Structure
```text
Sales-Data-Analysis/
├── data/
│   ├── raw/
│   └── cleaned/
├── notebooks/
│   └── sales_analysis.ipynb
├── scripts/
│   ├── generate_dataset.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   ├── sql_analysis.py
│   └── build_notebook.py
├── sql/
│   └── sales_queries.sql
├── outputs/
├── reports/
│   └── business_insights.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset Description
**Disclaimer:** The dataset used in this project (`data/raw/sales_data.csv`) is a **synthetic dataset** created specifically for learning and portfolio purposes. It contains approximately 250 records of simulated sales transactions across various products, categories, and regions.

## Data Cleaning Steps
The `data_cleaning.py` script performs the following operations:
1. Standardizes column names (lowercase, underscores).
2. Converts dates to `datetime` objects and amounts to numeric types.
3. Handles missing values and standardizes text capitalization.
4. Removes duplicate records.
5. Recalculates the `sales_amount` ensuring mathematical accuracy.

## Business Questions Answered
- What is the total revenue and number of orders?
- What is the average order value (AOV)?
- Which products and categories perform best?
- How do sales compare across different regions?
- What does the monthly sales trend look like?
- Who are the top 5 customers?

## How to Install Dependencies
1. Clone this repository.
2. Open Windows PowerShell and navigate to the project directory.
3. Run the following commands to set up the virtual environment and install packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## How to Run the Project
Ensure your virtual environment is activated, then run the scripts in this exact order:

```powershell
python scripts/generate_dataset.py
python scripts/data_cleaning.py
python scripts/exploratory_analysis.py
python scripts/sql_analysis.py
```
*(Optional)* Generate the Jupyter Notebook programmatically:
```powershell
python scripts/build_notebook.py
```

## How to Open the Jupyter Notebook
To view the combined analysis and visualizations interactively:
```powershell
jupyter notebook notebooks/sales_analysis.ipynb
```

## Sample Outputs
Check the `outputs/` folder for generated charts:
- `monthly_sales.png`
- `product_performance.png`
- `regional_sales.png`
- `category_sales.png`
- `sales_summary.csv`

The business insights are documented in `reports/business_insights.md`.

## Key Learnings
- Building an end-to-end data pipeline from raw data generation to final insights.
- Practical experience with Pandas for data wrangling and cleaning.
- Creating business-oriented visualizations.
- Integrating SQL analysis within a Python workflow using SQLite.

## Future Improvements
- Implement machine learning models for sales forecasting.
- Create an interactive dashboard using Streamlit or Dash.
- Connect to a remote database (e.g., PostgreSQL) instead of SQLite.
