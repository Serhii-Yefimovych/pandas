import pandas as pd
df = pd.read_csv('citibike.csv')
head = df.head(10)
print(head.to_string())
