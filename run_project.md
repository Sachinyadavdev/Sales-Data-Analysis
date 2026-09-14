# Step-by-Step Instructions to Run the Project

## 1.Activate the Virtual Environment:

.\.venv\Scripts\Activate.ps1

## 2. Execute the Data Pipeline (in this exact order):

python scripts/generate_dataset.py
python scripts/data_cleaning.py
python scripts/exploratory_analysis.py
python scripts/sql_analysis.py

## 3. SQL Database

In this project, we use **SQLite**, which is a lightweight, serverless database engine built directly into Python. You do not need to install MySQL, PostgreSQL, or any external database software.

Here is how it works:
1. The `scripts/sql_analysis.py` script reads the cleaned data from `cleaned_sales_data.csv` using Pandas.
2. It creates a local database file named `sales_analysis.db` in your project folder.
3. It takes the Pandas DataFrame and inserts it into a SQL table named `sales`.
4. It then runs standard SQL queries (like `SELECT`, `GROUP BY`, `SUM`) against this table to calculate metrics.
5. Finally, the script prints the results and closes the database connection. 

The `sql/sales_queries.sql` file contains the exact same queries for your reference and portfolio documentation.

## 4. Open the Notebook:

jupyter notebook notebooks/sales_analysis.ipynb

## 5. Items for Manual Review

- Notebook: Please open notebooks/sales_analysis.ipynb within Jupyter and run the cells from top to bottom to ensure you are happy with how the layout and markdown formatting appears.
- Outputs: Review the generated PNG files inside the outputs/ folder (monthly_sales.png, product_performance.png, category_sales.png, regional_sales.png) to ensure they look good for your portfolio.
- README: Take a look at the README.md and add your name or extra customization before uploading to GitHub.

# SQL Database
