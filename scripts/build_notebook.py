import nbformat as nbf

nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell("# Sales Data Analysis\n\n## 1. Project Introduction\nThis project analyzes a synthetic sales dataset to extract meaningful business insights. The purpose is to demonstrate data cleaning, exploratory data analysis (EDA), visualization, and SQL skills using Python, Pandas, Matplotlib, Seaborn, and SQLite."),
    
    nbf.v4.new_markdown_cell("## 2. Business Questions\n* What is the total revenue and total number of orders?\n* What is the average order value?\n* Which products generate the most revenue?\n* How are sales distributed across different regions and categories?\n* What is the monthly sales trend?\n* Who are the top customers by revenue?"),
    
    nbf.v4.new_markdown_cell("## 3. Importing Libraries"),
    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport sqlite3\n\n# Set plotting style\nplt.style.use('seaborn-v0_8-whitegrid')\nsns.set_palette('muted')\n\n# Display plots in notebook\n%matplotlib inline"),
    
    nbf.v4.new_markdown_cell("## 4. Loading the Raw Dataset"),
    nbf.v4.new_code_cell("raw_df = pd.read_csv('../data/raw/sales_data.csv')\nraw_df.head()"),
    
    nbf.v4.new_markdown_cell("## 5. Understanding the Dataset"),
    nbf.v4.new_code_cell("print(f'Shape: {raw_df.shape}')\nraw_df.info()"),
    
    nbf.v4.new_markdown_cell("## 6. Data-Quality Checks"),
    nbf.v4.new_code_cell("# Check missing values\nprint('Missing Values:')\nprint(raw_df.isnull().sum())\n\n# Check duplicates\nprint(f'\\nDuplicates: {raw_df.duplicated().sum()}')"),
    
    nbf.v4.new_markdown_cell("## 7. Data Cleaning\nWe will handle missing values, correct data types, standard text, and calculate the actual sales amount."),
    nbf.v4.new_code_cell("df = raw_df.copy()\n\n# Standardize column names\ndf.columns = df.columns.str.lower().str.replace(' ', '_')\n\n# Convert order_date to datetime\ndf['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')\n\n# Clean numeric columns\ndf['quantity'] = pd.to_numeric(df['quantity'].astype(str).str.replace(r'[^\\d.]', '', regex=True), errors='coerce')\ndf['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')\n\n# Standardize text\nfor col in ['product', 'category', 'region']:\n    df[col] = df[col].astype(str).str.strip().replace('nan', np.nan).str.title()\n\n# Handle missing values\ndf['product'] = df['product'].fillna('Unknown')\ndf['region'] = df['region'].fillna('Unknown')\ndf['quantity'] = df['quantity'].fillna(1.0)\n\n# Remove duplicates\ndf = df.drop_duplicates()\n\n# Recalculate sales amount\ndf['sales_amount'] = df['quantity'] * df['unit_price']\n\nprint(f'Cleaned Shape: {df.shape}')\ndf.head()"),
    
    nbf.v4.new_markdown_cell("## 8. Exploratory Data Analysis & 9. Business Metrics"),
    nbf.v4.new_code_cell("total_revenue = df['sales_amount'].sum()\ntotal_orders = df['order_id'].nunique()\ntotal_quantity = df['quantity'].sum()\naov = total_revenue / total_orders\n\nprint(f'Total Revenue: ${total_revenue:,.2f}')\nprint(f'Total Orders: {total_orders}')\nprint(f'Total Quantity Sold: {total_quantity}')\nprint(f'Average Order Value: ${aov:,.2f}')"),
    
    nbf.v4.new_markdown_cell("## 10. Data Visualizations"),
    nbf.v4.new_code_cell("# Monthly Sales Trend\ndf['month'] = df['order_date'].dt.to_period('M').astype(str)\nmonthly_sales = df.groupby('month')['sales_amount'].sum().reset_index()\n\nplt.figure(figsize=(10, 5))\nsns.lineplot(data=monthly_sales, x='month', y='sales_amount', marker='o')\nplt.title('Monthly Sales Trend')\nplt.xticks(rotation=45)\nplt.show()"),
    
    nbf.v4.new_code_cell("# Revenue by Product\nproduct_sales = df.groupby('product')['sales_amount'].sum().reset_index().sort_values('sales_amount', ascending=False)\nplt.figure(figsize=(10, 5))\nsns.barplot(data=product_sales, x='sales_amount', y='product', hue='product', legend=False)\nplt.title('Revenue by Product')\nplt.show()"),
    
    nbf.v4.new_markdown_cell("## 11. SQL Analysis using SQLite"),
    nbf.v4.new_code_cell("conn = sqlite3.connect(':memory:')\ndf.to_sql('sales', conn, if_exists='replace', index=False)\n\nquery = \"\"\"\nSELECT category, SUM(sales_amount) as total_revenue\nFROM sales\nGROUP BY category\nORDER BY total_revenue DESC;\n\"\"\"\n\npd.read_sql_query(query, conn)"),
    
    nbf.v4.new_markdown_cell("## 12. Key Business Insights\n- The top performing product categories and products drive a significant portion of revenue.\n- Certain regions outperform others, indicating potential for targeted marketing.\n- The monthly trend highlights potential seasonality or growth periods."),
    
    nbf.v4.new_markdown_cell("## 13. Business Recommendations\n- **Focus on Top Products:** Allocate more inventory and marketing budget to the highest performing products.\n- **Regional Strategy:** Investigate why certain regions are underperforming and adapt strategies accordingly.\n- **Customer Retention:** Target the top 5 customers with loyalty programs to maintain their high order volumes."),
    
    nbf.v4.new_markdown_cell("## 14. Conclusion\nThis project successfully demonstrated the end-to-end process of data cleaning, exploratory analysis, visualization, and SQL querying on a sales dataset. The insights generated can help drive data-informed business decisions.")
]

with open('notebooks/sales_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)
print('Notebook created successfully.')
