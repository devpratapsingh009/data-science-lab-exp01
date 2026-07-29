import pandas as pd

# Load dataset
df = pd.read_csv("train.csv")

# Display first 5 rows
print("=== Dataset Head ===")
print(df.head())

# Dataset Information
print("\n=== Dataset Info ===")
df.info()

# Summary Statistics
print("\n=== Summary Statistics ===")
print(df.describe())

# Missing Values
print("\n=== Missing Values ===")
print(df.isnull().sum())