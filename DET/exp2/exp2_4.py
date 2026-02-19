import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib as mplot

print("Loading dataset")
df = pd.read_csv('patient_health.csv')

print("Patient Health Data:")
print(df)

print("\nDataFrame Operations")

print("\nFirst 5 records:")
print(df.head())

print("\nSorted by Age (descending):")
sorted_df = df.sort_values('Age', ascending=False)
print(sorted_df.head(10))

print("\nPatients with Cholesterol > 200:")
filtered_df = df[df['Cholesterol'] > 200]
print(filtered_df)

print("\nRemoving Duplicates")
print(f"Records before: {len(df)}")
df = df.drop_duplicates()
print(f"Records after: {len(df)}")

print("\nHandling Missing Values")
print("Missing values before:")
print(df.isnull().sum())

health_cols = ['Age', 'Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic', 'Cholesterol', 'Sugar_Level']
imputer = SimpleImputer(strategy='mean')
df[health_cols] = imputer.fit_transform(df[health_cols])

print("\nMissing values after:")
print(df.isnull().sum())

print("\nStatistical Measures")

for col in health_cols:
    print(f"\n{col}:")
    print(f"  Mean: {df[col].mean():.2f}")
    print(f"  Median: {df[col].median():.2f}")
    print(f"  Std Dev: {df[col].std():.2f}")

print("\nMin-Max Normalization")

minmax_scaler = MinMaxScaler()
minmax_values = minmax_scaler.fit_transform(df[health_cols])
minmax_cols = [col + '_MinMax' for col in health_cols]
df[minmax_cols] = minmax_values

print("Min-Max normalized columns added")
print(df[['Patient_ID', 'Cholesterol', 'Cholesterol_MinMax', 'Sugar_Level', 'Sugar_Level_MinMax']].head())

print("\nZ-Score Normalization")

zscore_scaler = StandardScaler()
zscore_values = zscore_scaler.fit_transform(df[health_cols])
zscore_cols = [col + '_ZScore' for col in health_cols]
df[zscore_cols] = zscore_values

print("Z-Score normalized columns added")
print(df[['Patient_ID', 'Cholesterol', 'Cholesterol_ZScore', 'Sugar_Level', 'Sugar_Level_ZScore']].head())

print("\nCorrelation Analysis")
correlation_df = df[health_cols].corr()
print(correlation_df)

print("\nReducing Dataset")
print(f"Columns before: {list(df.columns)}")

essential_cols = ['Patient_ID', 'Name', 'Age', 'Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic',
                  'Cholesterol', 'Sugar_Level', 'Cholesterol_MinMax', 'Sugar_Level_MinMax',
                  'Cholesterol_ZScore', 'Sugar_Level_ZScore']
reduced_df = df[essential_cols]

print(f"Columns after: {list(reduced_df.columns)}")

print("\nValidation")
print(f"Total records: {len(reduced_df)}")
print(f"Total columns: {len(reduced_df.columns)}")
print(f"Missing values: {reduced_df.isnull().sum().sum()}")
print(f"Duplicate records: {reduced_df.duplicated().sum()}")

print("\nFinal Dataset:")
print(reduced_df)

reduced_df.to_csv('patient_health_final.csv', index=False)
print("\nDataset saved to patient_health_final.csv")
