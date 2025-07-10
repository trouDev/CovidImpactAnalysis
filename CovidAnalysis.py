import pandas as pd 

df = pd.read_csv("owid-covid-data.csv")

print(df.shape)
print(df.columns)
df.head()