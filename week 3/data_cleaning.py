import pandas as pd

df = pd.read_csv("messy_data.csv")

print("Original Data")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

df["Department"] = df["Department"].fillna("Unknown")

filtered_df = df[df["Salary"] > 55000]

df["Bonus"] = df["Salary"] * 0.10

print("\nCleaned Data")
print(df)

print("\nFiltered Data")
print(filtered_df)

df.to_csv("cleaned_data.csv", index=False)

print("\nFile saved as cleaned_data.csv")