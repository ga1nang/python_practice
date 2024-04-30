import pandas as pd

data = pd.read_csv("file\menu.csv")
data.describe()
data.info()
data.head(5)
data.tail(10)