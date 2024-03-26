import pandas as pd


data = pd.read_csv("schema.csv")

# rename column Friendly name to name

data.rename(columns={"Friendly Name": "Name"}, inplace=True)

data.to_csv("schema.csv", index=False)