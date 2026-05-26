import pandas as pd

data_frame = pd.read_csv("squirrel_data.csv")

series = data_frame["Primary Fur Color"].dropna()
counts = series.value_counts()

data = {
    "Color": pd.unique(series),
    "Count": counts.to_list()
}

df = pd.DataFrame(data)
df.to_csv("squirrel_count.csv", index=False)

