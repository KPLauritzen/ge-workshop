import pandas as pd
from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
df["target"] = boston.target

df.to_csv("data/raw_data.csv")