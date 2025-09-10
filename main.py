import pandas as pd

df = pd.read_csv("train.csv")   # or a path like "data/train.csv" if it lives in a subfolder
print(df.head())