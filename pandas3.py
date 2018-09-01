import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url,  sep='|')
F = users[users['gender']=='F'].groupby('occupation')['gender'].count()
M = users[users['gender']=='M'].groupby('occupation')['gender'].count()
F.rename('Fgen', inplace=True)
M.rename('Mgen', inplace=True)
MF = pd.concat([F, M], axis=1, join='inner')
MF['ratio'] = MF['Fgen'] / MF['Mgen']
print(MF)

# print (users.head(10)) # default value is 5
# print (users.tail(10)) # default value is 5
# # print(users.describe())
# import numpy as np
# print('-----------------------------------')
# print(users.shape)
# print('-----------------------------------')
# print(list(users))
# print('-----------------------------------')
# mf = users.groupby('gender').size()
# print(users.groupby('gender').age.mean())
# # print(type(mf))
# print(users.groupby('occupation').age.mean())
# df = pd.DataFrame(users)
# df = users.sort_values(by=['occupation','gender'])
# df['ratio'] = df.groupby('occupation')['gender'].div()
# df['ratio'] = df.groupby('occupation', 'gender')['ratio'].cumsum()
# print(df)

# print(users)

# grouped = users.groupby(['gender', 'occupation']).count()

# print(grouped)


# F.rename(columns={'gender': 'Fgen'}, inplace=True)
# M.rename(columns={'gender': 'Mgen'}, inplace=True)
# print(type(F))
# print(F)


# MF['ratio']=6
# print(users.groupby(['occupation', 'gender']).df.gender[['gender'], ['F']].count())
# xxx.pct_change(periods=3)
# print(pd.DataFrame.mean(users['gender'] =='F'))
# list(df.values.T.tolist())
# df['ratio'] =users.groupby('occupation').apply(lambda s: s.gender('M')/s.gender('F')).values
# print(df[:])
# print(pd.crosstab(df['occupation'], df['age']).apply(lambda r:r.mean(), axis=1))
# print(df[ df['occupation']=='F'][:])