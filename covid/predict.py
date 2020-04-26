import pandas as pd

train = pd.read_csv("training.csv")

train["hypothesis"] = 0
train.loc[train.gender == "female", "hypothesis"] = 1

train["result"] = 0
train.loc[train.recovered == train["hypothesis"], "result"] = 1

print(train["result"].value_counts(normalize=True))