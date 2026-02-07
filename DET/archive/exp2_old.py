import pandas as pd
import numpy as np
import warnings

df = pd.read_csv('student_academic_data.csv')

print(df.head(10))
print(f"\nDataset shape: {df.shape}")
print(f"Total students: {len(df)}")

print("\nFirst 5:")
print(df.head())

print("\nLast 5:")
print(df.tail())

print("\nDataset Info:")
print(df.info())

print("\nTop 10 students by Math marks:")
print(df.nlargest(10, 'Math')[['StudentID', 'Name', 'Math', 'Science', 'English']])

print("\nStudents with Attendance >= 95:")
high_attendance = df[df['Attendance'] >= 95]
print(f"Count: {len(high_attendance)}")
print(high_attendance[['StudentID', 'Name', 'Attendance']])

print(f"\nDuplicate records: {df.duplicated().sum()}")

df = df.drop_duplicates(subset=['StudentID', 'Name'], keep='first')
print(f"Dataset shape after removing duplicates: {df.shape}")


print("\nMissing values count:")
print(df.isnull().sum())

print("\nPercentage of missing values:")
print((df.isnull().sum() / len(df) * 100).round(2))

print("\nFilling missing values with mean...")
df['Math'].fillna(df['Math'].mean(), inplace=True)
df['Science'].fillna(df['Science'].mean(), inplace=True)
df['English'].fillna(df['English'].mean(), inplace=True)
df['Attendance'].fillna(df['Attendance'].mean(), inplace=True)

df['TotalMarks'] = df['Math'] + df['Science'] + df['English']
df['AverageMarks'] = df[['Math', 'Science', 'English']].mean(axis=1)

print("\nDataset with calculated fields (first 10 rows):")
print(df[['StudentID', 'Name', 'Math', 'Science', 'English', 'TotalMarks', 'AverageMarks', 'Attendance']].head(10))

print("\nStatistical Summary:")
print(df[['Math', 'Science', 'English', 'Attendance']].describe().round(2))

print("\nMean of each subject:")
print(f"Math Mean: {df['Math'].mean():.2f}")
print(f"Science Mean: {df['Science'].mean():.2f}")
print(f"English Mean: {df['English'].mean():.2f}")
print(f"Attendance Mean: {df['Attendance'].mean():.2f}")

print("\nMedian of each subject:")
print(f"Math Median: {df['Math'].median():.2f}")
print(f"Science Median: {df['Science'].median():.2f}")
print(f"English Median: {df['English'].median():.2f}")

print("\nStandard Deviation:")
print(f"Math Std Dev: {df['Math'].std():.2f}")
print(f"Science Std Dev: {df['Science'].std():.2f}")
print(f"English Std Dev: {df['English'].std():.2f}")

df_normalized = df.copy()

columns_to_normalize = ['Math', 'Science', 'English', 'Attendance']

for col in columns_to_normalize:
    min_val = df[col].min()
    max_val = df[col].max()
    df_normalized[col] = (df[col] - min_val) / (max_val - min_val)

print("\nNormalized Data (0-1 range) - First 10 rows:")
print(df_normalized[['StudentID', 'Name'] + columns_to_normalize].head(10).round(3))

df_final = df[['StudentID', 'Name', 'Math', 'Science', 'English', 'AverageMarks', 'Attendance']].copy()

print("\nFinal Dataset (irrelevant columns removed) - First 10 rows:")
print(df_final.head(10))
print(f"\nColumns kept: {list(df_final.columns)}")
print(f"Columns removed: TotalMarks (redundant as we have AverageMarks)")

output_path = '/home/yash/college/DET/student_data_preprocessed.csv'
df_final.to_csv(output_path, index=False)

print("\nFinal Dataset Summary:")
print(f"Total records: {len(df_final)}")
print(df_final.describe().round(2))

