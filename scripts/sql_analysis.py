import pandas as pd
import sqlite3
import os

print("--- SQL Analysis with SQLite ---")

# 1. Load the cleaned CSV using Pandas
print("Loading cleaned dataset...")
df = pd.read_csv('data/cleaned/cleaned_sales_data.csv')

# 2. Create a SQLite database
db_path = 'sales_analysis.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
print(f"Connected to SQLite database: {db_path}")

# 3 & 4. Create a table named 'sales' and insert the dataset
df.to_sql('sales', conn, if_exists='replace', index=False)
print("Data successfully loaded into the 'sales' table.")

# 5. Execute SQL queries
queries = {
    "Total Revenue": """
        SELECT SUM(sales_amount) AS total_revenue 
        FROM sales;
    """,
    "Total Orders": """
        SELECT COUNT(DISTINCT order_id) AS total_orders 
        FROM sales;
    """,
    "Revenue by Product": """
        SELECT product, SUM(sales_amount) AS revenue 
        FROM sales 
        GROUP BY product 
        ORDER BY revenue DESC;
    """,
    "Revenue by Region": """
        SELECT region, SUM(sales_amount) AS revenue 
        FROM sales 
        GROUP BY region 
        ORDER BY revenue DESC;
    """,
    "Revenue by Category": """
        SELECT category, SUM(sales_amount) AS revenue 
        FROM sales 
        GROUP BY category 
        ORDER BY revenue DESC;
    """,
    "Monthly Revenue": """
        SELECT strftime('%Y-%m', order_date) AS month, SUM(sales_amount) AS revenue 
        FROM sales 
        GROUP BY month 
        ORDER BY month;
    """,
    "Top Five Customers": """
        SELECT customer_id, SUM(sales_amount) AS total_spent 
        FROM sales 
        GROUP BY customer_id 
        ORDER BY total_spent DESC 
        LIMIT 5;
    """,
    "Average Order Value": """
        SELECT SUM(sales_amount) / COUNT(DISTINCT order_id) AS avg_order_value 
        FROM sales;
    """,
    "Products with Total Quantity Sold > 10": """
        SELECT product, SUM(quantity) AS total_quantity 
        FROM sales 
        GROUP BY product 
        HAVING total_quantity > 10 
        ORDER BY total_quantity DESC;
    """
}

# 6. Print the query results clearly
print("\n--- SQL Query Results ---")
for title, query in queries.items():
    print(f"\n[{title}]")
    try:
        result_df = pd.read_sql_query(query, conn)
        print(result_df.to_string(index=False))
    except Exception as e:
        print(f"Error executing query: {e}")

# Close the connection
conn.close()
print("\nDatabase connection closed.")
