import pandas as pd
from sklearn.preprocessing import normalize
df = pd.read_csv("data/raw_data.csv")

# make some groups
group_cols = ["LSTAT", "INDUS"]
for col in group_cols:
    df[f"{col}_bins"] = pd.qcut(df[col], [0, .25, .5, .75, 1.])

# normalization
normed_cols = ["ZN", "CRIM"]
for col in normed_cols:
    df[col] = normalize(df[[col]])


df.to_csv("data/processed_data.csv")