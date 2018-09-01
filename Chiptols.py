import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
print(chipo.columns)
# print(chipo.shape)
# print(type('item_price'))
# print(chipo.loc[10:, ['order_id', 'item_price']])
# print(chipo.item_name.value_counts().head(1))
# print(chipo.item_name.value_counts().max())
#
# def conveDOL(x):
#     new = x.replace('$', '')
#     return float(new)
#print(chipo['item_price'].apply(conveDOL).head())
#print((chipo['item_price'].apply(conveDOL)*chipo['quantity']).sum())
#print((chipo['item_price'].apply(conveDOL)).sum())
def conveDOL(x):
    new = x.replace('$', '')
    return float(new)


chipo.item_price = chipo.item_price.apply(conveDOL)
# print(chipo[:].head())
# print(len(chipo.order_id.unique()))
# print((chipo.item_price*chipo.quantity).sum())
# print(((chipo.item_price*chipo.quantity).sum())/(len(chipo.order_id.unique())))
# og = chipo.groupby(by=['order_id']).sum()
# print(og.mean()['item_price'])
# print(chipo.quantity.sum())
print('---------------------------------------')
# print(chipo.item_name.value_counts().sum())
# answer = chipo[chipo.item_name == "Veggie Salad Bowl"]
answer = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
print(len(answer))