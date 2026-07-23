import pandas as pd

df = pd.read_csv("student_dirty.csv")

print("Original Dataset")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

df = df.drop_duplicates()

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3

print("\nCleaned Dataset")
print(df)

df.to_csv("cleaned_student.csv", index=False)

print("\nDataset cleaned and saved successfully.")