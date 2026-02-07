import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv')

print(df.head())

print("DataFrame Info")
print(df.info())

print("Summary")
print(df.describe())

print("\nMean values:")
print(df.mean(numeric_only=True))

print("\nMedian values:")
print(df.median(numeric_only=True))

print("\nMode values (all columns):")
print(df.mode().iloc[0])

print("\nStandard deviation:")
print(df.std(numeric_only=True))


# max_marks_idx = df['Total_Marks'].idxmax()
# top_student = df.loc[max_marks_idx]
# print("\n5. STUDENT WITH HIGHEST TOTAL MARKS")
# print("-" * 60)
# print(f"Name: {top_student['Student_Name']}")
# print(f"Total Marks: {top_student['Total_Marks']}")
# print(f"Average Marks: {top_student['Average_Marks']:.2f}")
