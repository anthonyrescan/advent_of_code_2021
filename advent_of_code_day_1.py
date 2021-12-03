import pandas as pd
path = "day1.csv"

data = pd.read_csv(
        path,
        squeeze=True,
        header=None,
    )

p1 = (data.rolling(1).sum().diff().gt(0)).sum()
print(p1)
p2 = (data.rolling(3).sum().diff().gt(0)).sum()
print(p2)
