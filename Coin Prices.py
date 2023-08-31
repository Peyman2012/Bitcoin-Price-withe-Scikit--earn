import requests
import pandas as pd
from sklearn import preprocessing
from sklearn import tree
# data = requests.get('https://api.coincap.io/v2/assets')
data = requests.get('https://api.wazirx.com/sapi/v1/tickers/24hr')

d_data=data.json()


symbol=[]
open_price=[]
low_price=[]
high_price=[]
last_price=[]
bid_price=[]
ask_price=[]
volume=[]



for i in range(len(d_data)):
    symbol.append(d_data[i]['baseAsset'])
    open_price.append(d_data[i]['openPrice'])
    low_price.append(d_data[i]['lowPrice'])
    high_price.append(d_data[i]['highPrice'])
    bid_price.append(d_data[i]['bidPrice'])
    ask_price.append(d_data[i]['askPrice'])
    last_price.append(d_data[i]['lastPrice'])
    volume.append(d_data[i]['volume'])


dict_coins={'Symbol':symbol,'Open Price':open_price,'Low Price':low_price,'High Price':high_price,'Bid Price':bid_price,'Last Price':last_price,'Ask Price':ask_price
            ,'Volume':volume}
df_coins=pd.DataFrame(dict_coins)
# print(df_coins)
df_coins.to_csv('Coin Price.csv',index=False)

df=pd.read_csv('Coin Price.csv')
# print(df)
Symbol = df['Symbol']

le = preprocessing.LabelEncoder()
le.fit(Symbol)
df['Name label'] = le.transform(Symbol)
Name_label=df['Name label']
x=[]
y=[]


for i in range(len(df)):
    x.append([open_price[i],low_price[i],high_price[i],last_price[i]])
    y.append([Name_label[i]])
# print(Name_label)
print(x)
# print(y)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
new_data = [['2392999', '2350104.0', '2402000.0', '2371496.0'], ['46.7296', '45.5101', '47.0', '45.5267'], ['150000', '147000.1', '151400.0', '148998.9']]
answer = clf.predict(new_data)
for i in range(len(new_data)):
    df_name=df[df['Name label']==answer[i]]
    search_name = df_name['Symbol'].tolist()
    print(f'Cryptocurrency price your number {i+1} choice ====> {search_name[0]}')
