import pandas as pd
import sklearn.preprocessing as preprocessing
import matplotlib as mpl

df = pd.read_csv('student_attendance.csv')
print(df.head())

scaler = preprocessing.StandardScaler()
df_scaled = df.copy()
attendance_columns = ['Classes_Attended', 'Attendance_Percentage']
df_scaled[attendance_columns] = scaler.fit_transform(df[attendance_columns])



print(df_scaled.head())