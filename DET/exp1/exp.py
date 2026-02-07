import pandas as pd
import numpy as np

print("Student Academic Performance")

data = {
    'Student_Name': ['Aarav Sharma', 'Priya Singh', 'Rahul Verma', 'Sneha Patel',
                     'Vikram Desai', 'Ananya Iyer', 'Rohan Gupta', 'Meera Nair',
                     'Aditya Joshi', 'Kavya Menon'],
    'Mathematics': [85, 78, 92, 88, 76, 95, 81, 89, 77, 83],
    'English': [90, 85, 88, 92, 80, 91, 87, 94, 82, 88],
    'Science': [88, 82, 95, 87, 79, 93, 84, 91, 85, 86]
}

print("Dataframe created")
df = pd.DataFrame(data)
print(df)

print("\nFirst 5 rows")
print(df.head())

print("\nLast 5 rows")
print(df.tail())


df['Total_Marks'] = df['Mathematics'] + df['English'] + df['Science']
df['Average_Marks'] = df['Total_Marks'] / 3

print(df[['Student_Name', 'Total_Marks', 'Average_Marks']])


subjects = ['Mathematics', 'English', 'Science']
stats_data = []

for subject in subjects:
    mean_val = df[subject].mean()
    median_val = df[subject].median()
    std_val = df[subject].std()
    
    stats_data.append({
        'Subject': subject,
        'Mean': mean_val,
        'Median': median_val,
        'StandardDeviation': std_val
    })
    
    print(f"\n{subject}:")
    print(f"  Mean: {mean_val:.2f}")
    print(f"  Median: {median_val:.2f}")
    print(f"  Standard Deviation: {std_val:.2f}")

stats_df = pd.DataFrame(stats_data)

print("\n Checking missing values")
missing_values = df.isnull().sum()
print("Missing values in column:")
print(missing_values)

if missing_values.sum() > 0:
    print("\nHandling missing values")
    df = df.fillna(df.mean())
else:
    print("\nNo missing values found")

output_file = '/home/yash/college/DET/student_performance_processed.csv'
df.to_csv(output_file)
print(f"Processed data exported to: {output_file}")