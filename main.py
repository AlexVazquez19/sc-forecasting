import pandas as pd

df = pd.read_csv("Data/train.csv")   # or a path like "data/train.csv" if it lives in a subfolder
print(df.head())