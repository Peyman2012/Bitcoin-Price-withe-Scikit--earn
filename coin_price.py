import pandas as pd
import requests
from sklearn import preprocessing
from sklearn import tree

url = '	https://api.coinlore.net/api/tickers/'
r = requests.get(url)


coin_r=r.json()

c_coin=coin_r['data']

symbol=[]
name=[]
nameid=[]
rank=[]
price=[]
percent_change_24h=[]
percent_change_1h=[]
percent_change_7d=[]
price_btc=[]
market_cap_usd=[]
volume24=[]

for i in range(len(c_coin)):
    symbol.append(c_coin[i]['symbol'])
    name.append(c_coin[i]['name'])
    nameid.append(c_coin[i]['nameid'])
    rank.append(c_coin[i]['rank'])
    price.append(c_coin[i]['price_usd'])
    percent_change_24h.append(c_coin[i]['percent_change_24h'])
    percent_change_1h.append(c_coin[i]['percent_change_1h'])
    percent_change_7d.append(c_coin[i]['percent_change_7d'])
    price_btc.append(c_coin[i]['price_btc'])
    market_cap_usd.append(c_coin[i]['market_cap_usd'])
    volume24.append(c_coin[i]['volume24'])
dic={'Symbol Coin':symbol,'Name Coin':name,'NameId':nameid,'Rank Coin':rank,'Price Coin':price,'Percent Change 24h':percent_change_24h,
     'Percent Change 1h':percent_change_1h,'Percent Change 7d':percent_change_7d,'Market Cap USD':market_cap_usd,'Volume':volume24}
df=pd.DataFrame(dic)
print(df)
df.to_csv('Coin Price.csv',index=False)


Symbol = df['Symbol Coin']
Price = df['Price Coin']

le = preprocessing.LabelEncoder()
le.fit(Symbol)
df['Name label'] = le.transform(Symbol)
Name_label=df['Name label']
x=[]
y=[]


for i in range(len(df)):
    x.append([Price[i]])
    y.append([Name_label[i]])
# print(Name_label)
print(x)
# print(y)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
new_data = [['27254.35'], ['1704.05'], ['1.00'], ['223.40'], ['1.00'], ['0.524916']]
answer = clf.predict(new_data)
for i in range(len(new_data)):
    df_name=df[df['Name label']==answer[i]]
    search_name = df_name['Symbol Coin'].tolist()
    print(f'Cryptocurrency price your number {i+1} choice ====> {search_name[0]}')
