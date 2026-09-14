import pandas as pd
import numpy as np
import os

# Ensure the output directory exists
os.makedirs('data/cleaned', exist_ok=True)

print("--- Sales Data Cleaning Process ---")

# 1. Load data/raw/sales_data.csv
print("\n1. Loading raw dataset...")
df = pd.read_csv('data/raw/sales_data.csv')

# 2. Display the first five rows
print("\n2. First 5 rows of raw data:")
print(df.head())

# 3. Display the dataset shape and data types
print("\n3. Dataset info (Shape and Data Types):")
print(f"Shape: {df.shape}")
print(df.dtypes)

# 4. Check missing values
print("\n4. Missing values per column:")
print(df.isnull().sum())

# 5. Check duplicate records
print("\n5. Number of duplicate records:")
print(df.duplicated().sum())

# 6. Standardize column names using lowercase and underscores (Already mostly standard, but let's ensure it)
print("\n6. Standardizing column names...")
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 7. Convert order_date into a datetime column
print("\n7. Converting order_date to datetime...")
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# 8. Convert quantity, unit_price, and sales_amount into numeric values
print("\n8. Converting numeric columns...")
# Replacing any non-numeric characters (like spaces) before converting
df['quantity'] = pd.to_numeric(df['quantity'].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')

# 9. Standardize text columns by removing extra spaces
print("\n9. Standardizing text columns (stripping spaces)...")
text_cols = ['product', 'category', 'region', 'customer_id']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()
    # Replace 'nan' string back to actual NaN
    df[col] = df[col].replace('nan', np.nan)

# 10. Standardize product and region capitalization
print("\n10. Standardizing capitalization...")
df['product'] = df['product'].str.title()
df['region'] = df['region'].str.title()
df['category'] = df['category'].str.title()

# 11. Handle missing values using simple beginner-friendly logic
print("\n11. Handling missing values...")
# Fill missing categorical data with 'Unknown'
df['product'] = df['product'].fillna('Unknown')
df['region'] = df['region'].fillna('Unknown')

# Fill missing quantities with median or simply 1 for this context
df['quantity'] = df['quantity'].fillna(1.0)

# 12. Remove duplicate records
print("\n12. Removing duplicate records...")
df = df.drop_duplicates()
print(f"New shape after removing duplicates: {df.shape}")

# 13. Recalculate sales_amount using: sales_amount = quantity * unit_price
print("\n13. Recalculating sales_amount...")
df['sales_amount'] = df['quantity'] * df['unit_price']

# Final check of data info
print("\nCleaned Data Info:")
print(df.info())

# 14. Save the cleaned dataset
cleaned_path = 'data/cleaned/cleaned_sales_data.csv'
df.to_csv(cleaned_path, index=False)
print(f"\n14. Cleaned dataset saved successfully to: {cleaned_path}")
