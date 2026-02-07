import pandas as pd
import numpy as np

personal_df = pd.read_csv('employee_personal_details.csv')
salary_df = pd.read_csv('employee_salary_details.csv')

print(f"Personal Details Dataset Shape: {personal_df.shape}")
print(f"Salary Details Dataset Shape: {salary_df.shape}")
print("\nPersonal Details Dataset (First 5 rows):")
print(personal_df.head())
print("\nSalary Details Dataset (First 5 rows):")
print(salary_df.head())

integrated_df = pd.merge(personal_df, salary_df, on='Employee_ID', how='inner')
print(f"Integrated Dataset Shape: {integrated_df.shape}")
print("\nIntegrated Dataset (First 5 rows):")
print(integrated_df.head())

print(integrated_df.describe())

print("\nMissing values before cleaning:")
missing = integrated_df.isnull().sum()
print(missing)

integrated_df = integrated_df.dropna()
