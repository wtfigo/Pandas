from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')
table_names = engine.table_names()
df = pd.read_sql_query('SELECT * FROM Invoice', engine)
print('The average is:', df.loc[:, 'Total'].sum()/df.loc[:, 'Total'].count())

def med(x):
    sorted_x=sorted(x)
    length_n=len(x)
    middle=length_n//2
    if length_n % 2 == 0:
        med_even = sorted_x[middle - 1]+sorted_x[middle] / 2
        return(med_even)
    else:
        return(sorted_x[middle])
df_list = df.Total.tolist()
print('median is: ', med(df_list))


# print(df.describe())
# print(df.count(axis=0))
# print(df[:])
# l=(int(round(len(df))/2))
# print(l)
# print(df.shape)
# print(df.loc[l-6:l+6,['Total']].Total.sort_values())
# print(df.Total.describe())
# print(df.Total.median())
