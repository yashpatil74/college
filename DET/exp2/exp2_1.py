import pandas as pd

print("Loading datasets")
academic_df = pd.read_csv('student_academic.csv')
attendance_df = pd.read_csv('student_attendance.csv')

print("Academic Data:")
print(academic_df)
print("\nAttendance Data:")
print(attendance_df)

print("\nDataFrame Operations")

print("\nFirst 5 records:")
print(academic_df.head())

print("\nSorted by Math marks (descending):")
sorted_df = academic_df.sort_values('Math', ascending=False)
print(sorted_df.head(10))

print("\nStudents with Math > 80:")
filtered_df = academic_df[academic_df['Math'] > 80]
print(filtered_df)

print("\nRemoving Duplicates")
print(f"Records before: {len(academic_df)}")
academic_df = academic_df.drop_duplicates()
print(f"Records after: {len(academic_df)}")

print("\nHandling Missing Values")
print("Missing values before:")
print(academic_df.isnull().sum())

academic_df['Math'] = academic_df['Math'].fillna(academic_df['Math'].mean())
academic_df['Science'] = academic_df['Science'].fillna(academic_df['Science'].mean())
academic_df['English'] = academic_df['English'].fillna(academic_df['English'].mean())
academic_df['History'] = academic_df['History'].fillna(academic_df['History'].mean())
academic_df['Computer'] = academic_df['Computer'].fillna(academic_df['Computer'].mean())

print("\nMissing values after:")
print(academic_df.isnull().sum())

print("\nIntegrating Datasets")
integrated_df = pd.merge(academic_df, attendance_df, on='Student_ID')
print(f"Integrated dataset shape: {integrated_df.shape}")
print(integrated_df.head(10))

print("\nStatistical Measures")
subjects = ['Math', 'Science', 'English', 'History', 'Computer']

for subject in subjects:
    print(f"\n{subject}:")
    print(f"  Mean: {integrated_df[subject].mean():.2f}")
    print(f"  Median: {integrated_df[subject].median():.2f}")
    print(f"  Std Dev: {integrated_df[subject].std():.2f}")

print("\nNormalization (Min-Max)")

for subject in subjects:
    min_val = integrated_df[subject].min()
    max_val = integrated_df[subject].max()
    integrated_df[subject + '_Normalized'] = (integrated_df[subject] - min_val) / (max_val - min_val)

print("Normalized columns added:")
print(integrated_df[['Student_ID', 'Math', 'Math_Normalized', 'Science', 'Science_Normalized']].head())

print("\nReducing Dataset")
print(f"Columns before: {list(integrated_df.columns)}")

essential_cols = ['Student_ID', 'Name', 
                  'Attendance_Percentage', 'Math_Normalized', 'Science_Normalized', 
                  'English_Normalized', 'History_Normalized', 'Computer_Normalized']
reduced_df = integrated_df[essential_cols]

print(f"Columns after: {list(reduced_df.columns)}")

print("\nValidation")
print(f"Total records: {len(reduced_df)}")
print(f"Total columns: {len(reduced_df.columns)}")
print(f"Missing values: {reduced_df.isnull().sum().sum()}")
print(f"Duplicate records: {reduced_df.duplicated().sum()}")

print("\nFinal Dataset:")
print(reduced_df)

reduced_df.to_csv('student_preprocessed_final.csv', index=False)
print("\nDataset saved to student_preprocessed_final.csv")
