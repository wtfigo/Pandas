import pandas as pd

data1 = {'a': [1, 2, 3], 'b': [4, 5, 6]}
data2 = {'a': [7, 8, 9], 'b': [10, 11, 12]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df3 = pd.merge(df1, df2, on='b', suffixes=('_x', '_y'))
print(df3)