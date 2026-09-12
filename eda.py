import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/student_performance.csv"

df = pd.read_csv(DATA_PATH)
print("Shape before cleaning:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates().copy()

for col in ["Study_Hours_Per_Day", "Assignment_Score"]:
    df[col] = df[col].fillna(df[col].median())

print("\nShape after cleaning:", df.shape)
print("\nDescriptive statistics:\n", df.describe())

plt.hist(df["Final_Marks"], bins=12)
plt.title("Distribution of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.show()
