import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Ensure the data directory exists
os.makedirs('data/raw', exist_ok=True)

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define dataset parameters
num_records = 250

categories = {
    'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Monitor'],
    'Furniture': ['Desk', 'Chair', 'Bookshelf', 'Sofa'],
    'Office Supplies': ['Pens', 'Notebook', 'Paper', 'Stapler'],
    'Accessories': ['Mouse', 'Keyboard', 'Headphones', 'Webcam']
}
regions = ['North', 'South', 'East', 'West']

# Generate basic data
data = []
start_date = datetime(2023, 1, 1)

for i in range(1, num_records + 1):
    order_id = f"ORD-{i:04d}"
    order_date = start_date + timedelta(days=random.randint(0, 365))
    
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    region = random.choice(regions)
    
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(10.0, 1000.0), 2)
    sales_amount = round(quantity * unit_price, 2)
    customer_id = f"CUST-{random.randint(100, 150):04d}"
    
    data.append([order_id, order_date.strftime('%Y-%m-%d'), product, category, region, quantity, unit_price, sales_amount, customer_id])

df = pd.DataFrame(data, columns=['order_id', 'order_date', 'product', 'category', 'region', 'quantity', 'unit_price', 'sales_amount', 'customer_id'])

# Introduce intentional data quality issues for cleaning practice
# 1. Missing product values
missing_prod_idx = random.sample(range(num_records), 10)
df.loc[missing_prod_idx, 'product'] = np.nan

# 2. Missing region values
missing_reg_idx = random.sample(range(num_records), 8)
df.loc[missing_reg_idx, 'region'] = np.nan

# 3. Duplicate order records
duplicates = df.sample(5)
df = pd.concat([df, duplicates], ignore_index=True)

# 4. Inconsistent capitalization
mixed_case_idx = random.sample(range(len(df)), 15)
for idx in mixed_case_idx:
    if pd.notna(df.at[idx, 'region']):
        df.at[idx, 'region'] = df.at[idx, 'region'].upper()
    if pd.notna(df.at[idx, 'product']):
        df.at[idx, 'product'] = df.at[idx, 'product'].lower()

# 5. Some numeric values stored as strings
df['quantity'] = df['quantity'].astype(object)
string_num_idx = random.sample(range(len(df)), 12)
for idx in string_num_idx:
    df.at[idx, 'quantity'] = str(df.at[idx, 'quantity']) + " " # add a space to make it dirty

# Save the raw dataset
df.to_csv('data/raw/sales_data.csv', index=False)
print("Synthetic raw dataset generated successfully at data/raw/sales_data.csv")
