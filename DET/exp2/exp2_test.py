import pandas as pd
import sklearn.preprocessing as preprocessing

df = pd.read_csv('patient_health.csv')

print("Original Dataset:")
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")

numeric_columns = ['Age', 'Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic', 
                   'Cholesterol', 'Sugar_Level']

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

print(f"\n filling missing values:\n{df.isnull().sum()}")

df_cleaned = df.drop_duplicates()
print(f"\nDataset shape after removing duplicates")

scaler = preprocessing.MinMaxScaler()
df_normalized = df_cleaned.copy()
df_normalized[numeric_columns] = scaler.fit_transform(df_cleaned[numeric_columns])

print("Normalized Dataset (first 10 rows):")
print(df_normalized.head(10))

print("Statistics of Normalized Data:")
print(df_normalized[numeric_columns].describe())

df_normalized.to_csv('patient_health_normalized.csv', index=False)
print("\n dataset saved to 'patient_health_normalized.csv'")
