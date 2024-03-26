import pandas as pd


with open("from_measures.txt") as f:
    rows = f.read()


col_lenghts={}

res=[]


for line in rows.split("\n"):
    cols = line.split("|")
    col_lenghts[len(cols)] = col_lenghts.get(len(cols), 0) + 1
    cols = [col.strip() for col in cols]
    if len(cols) != 5:
        print(cols)
    res.append(cols[1:])

print(col_lenghts)


# make pandas dataframe
df = pd.DataFrame(res[1:], columns=res[0])

df.to_csv("measures_schema.csv", index=False)