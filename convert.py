import pandas as pd


data = pd.read_csv("schema.csv")

data.drop(columns=['Description'], inplace=True)

data.to_csv("schema.csv", index=False)