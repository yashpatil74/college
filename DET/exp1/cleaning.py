import pandas as pd
import numpy as np

df = pd.read_csv('retail_store_sales.csv')

print(df.head())    

print("DataFrame Info")
print(df.info())

print("Summary")
print(df.describe())

print("Checking for missing values")
missing_values = df.isnull().sum()
print(missing_values)

print("Deleting null values")
df_cleaned = df.dropna()

print("Checking for duplicate values")
duplicate_values = df_cleaned.duplicated().sum()
print(f"Duplicate rows: {duplicate_values}")