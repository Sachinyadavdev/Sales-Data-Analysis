import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the output directory exists
os.makedirs('outputs', exist_ok=True)

# Set styling for plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("muted")

print("--- Exploratory Data Analysis ---")

# 1. Load the cleaned dataset
print("Loading cleaned dataset...")
df = pd.read_csv('data/cleaned/cleaned_sales_data.csv')

# Ensure order_date is datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# --- Business Metrics Calculations ---

# Total revenue
total_revenue = df['sales_amount'].sum()
# Total number of orders (assuming one row = one order item, unique orders by order_id)
total_orders = df['order_id'].nunique()
# Total quantity sold
total_quantity = df['quantity'].sum()
# Average order value
aov = total_revenue / total_orders

print(f"\n--- Key Metrics ---")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Order Value: ${aov:,.2f}")

# Monthly revenue
# Extract month for grouping (YYYY-MM)
df['month'] = df['order_date'].dt.to_period('M')
monthly_revenue = df.groupby('month')['sales_amount'].sum().reset_index()
monthly_revenue['month'] = monthly_revenue['month'].astype(str)

# Revenue by product
product_revenue = df.groupby('product')['sales_amount'].sum().reset_index().sort_values('sales_amount', ascending=False)

# Quantity sold by product
product_quantity = df.groupby('product')['quantity'].sum().reset_index().sort_values('quantity', ascending=False)

# Revenue by category
category_revenue = df.groupby('category')['sales_amount'].sum().reset_index().sort_values('sales_amount', ascending=False)

# Revenue by region
region_revenue = df.groupby('region')['sales_amount'].sum().reset_index().sort_values('sales_amount', ascending=False)

# Top five customers by revenue
top_customers = df.groupby('customer_id')['sales_amount'].sum().reset_index().sort_values('sales_amount', ascending=False).head(5)

# Save a summary file
summary_data = {
    'Metric': ['Total Revenue', 'Total Orders', 'Total Quantity', 'Average Order Value'],
    'Value': [total_revenue, total_orders, total_quantity, aov]
}
pd.DataFrame(summary_data).to_csv('outputs/sales_summary.csv', index=False)
print("\nSummary metrics saved to outputs/sales_summary.csv")

# --- Visualizations ---

print("\nGenerating visualizations...")

# 1. Monthly sales trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_revenue, x='month', y='sales_amount', marker='o')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/monthly_sales.png')
plt.close()

# 2. Revenue by product
plt.figure(figsize=(10, 6))
sns.barplot(data=product_revenue, x='sales_amount', y='product', hue='product', legend=False)
plt.title('Revenue by Product', fontsize=14)
plt.xlabel('Revenue ($)', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.tight_layout()
plt.savefig('outputs/product_performance.png')
plt.close()

# 3. Revenue by region
plt.figure(figsize=(8, 6))
sns.barplot(data=region_revenue, x='region', y='sales_amount', hue='region', legend=False)
plt.title('Revenue by Region', fontsize=14)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.tight_layout()
plt.savefig('outputs/regional_sales.png')
plt.close()

# 4. Revenue by category
plt.figure(figsize=(8, 8))
plt.pie(category_revenue['sales_amount'], labels=category_revenue['category'], autopct='%1.1f%%', startangle=140)
plt.title('Revenue Share by Category', fontsize=14)
plt.tight_layout()
plt.savefig('outputs/category_sales.png')
plt.close()

print("Visualizations saved to the outputs/ directory.")
