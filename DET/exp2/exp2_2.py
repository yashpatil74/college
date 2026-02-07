import pandas as pd

print("Loading datasets")
personal_df = pd.read_csv('employee_personal.csv')
salary_df = pd.read_csv('employee_salary.csv')

print("Personal Details:")
print(personal_df)
print("\nSalary Details:")
print(salary_df)

print("\nMerging datasets")
merged_df = pd.merge(personal_df, salary_df, on='Employee_ID')
print(merged_df)

print("\nCleaning data")
print("Missing values before cleaning:")
print(merged_df.isnull().sum())

merged_df['Age'] = merged_df['Age'].fillna(merged_df['Age'].mean())
merged_df['Email'] = merged_df['Email'].fillna('unknown@email.com')
merged_df['Phone'] = merged_df['Phone'].fillna(0)
merged_df['HRA'] = merged_df['HRA'].fillna(merged_df['HRA'].mean())
merged_df['DA'] = merged_df['DA'].fillna(merged_df['DA'].mean())
merged_df['Bonus'] = merged_df['Bonus'].fillna(merged_df['Bonus'].mean())

merged_df = merged_df.drop_duplicates()

print("\nMissing values after cleaning:")
print(merged_df.isnull().sum())
print("\nRows after removing duplicates:", len(merged_df))

print("\nGrouping by Department")
dept_group = merged_df.groupby('Department')['Basic_Salary'].mean()
print(dept_group)

print("\nTotal salary by department:")
print(merged_df.groupby('Department')['Basic_Salary'].sum())

print("\nEmployee count by department:")
print(merged_df.groupby('Department')['Employee_ID'].count())

print("\nStatistical Measures")
print("Mean salary:", merged_df['Basic_Salary'].mean())
print("Median salary:", merged_df['Basic_Salary'].median())
print("Standard deviation:", merged_df['Basic_Salary'].std())
print("Min salary:", merged_df['Basic_Salary'].min())
print("Max salary:", merged_df['Basic_Salary'].max())

print("\nNormalizing Salary")
min_sal = merged_df['Basic_Salary'].min()
max_sal = merged_df['Basic_Salary'].max()
merged_df['Normalized_Salary'] = (merged_df['Basic_Salary'] - min_sal) / (max_sal - min_sal)
print(merged_df[['Name', 'Basic_Salary', 'Normalized_Salary']])

print("\nReducing dataset")
reduced_df = merged_df[['Employee_ID', 'Name', 'Department', 'Age', 'Basic_Salary', 'Normalized_Salary']]
print(reduced_df)

print("\nValidation")
print("Total rows:", len(reduced_df))
print("Total columns:", len(reduced_df.columns))
print("Missing values:", reduced_df.isnull().sum().sum())
print("Duplicate rows:", reduced_df.duplicated().sum())
print("Data types:")
print(reduced_df.dtypes)

reduced_df.to_csv('employee_final.csv', index=False)
print("\nFinal dataset saved to employee_final.csv")
print("\nFinal Dataset:")
print(reduced_df)
