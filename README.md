
![Bitcoin-Cryptocurrency-Placeholder](https://github.com/Peyman2012/Cryptocurrency-price-with-Scikit-learn/assets/88220773/f84ff9d4-d663-45c9-8cce-1ee23e26f02f)

**Cryptocurrency-price-with-Scikit-learn**

Library required for the project:

      import requests
      import pandas as pd
      from sklearn import preprocessing
      from sklearn import tree

Getting site information by using API, we get the price of cryptocurrencies.
 requests.get(), we get the information that the site has provided to the programmers:

      url = 'https://api.coinlore.net/api/tickers/'
      r = requests.get(url)

We cannot use classification in this project because the classifier generally separates distinct classes, and so this classifier expects a string or an integer type to distinguish different classes from each other (this is called the "target " Is known). You can read more about this in Introduction to Classifiers.

The problem we are trying to solve is to determine a continuous numerical output, Result. This is known as a regression problem, so we need to use a regression algorithm (such as DecisionTreeRegressor).

      clf = tree.DecisionTreeClassifier()
      clf = clf.fit(x, y)
      new_data = [['27254.35'], ['1704.05'], ['1.00'], ['223.40'], ['1.00'], ['0.524916']]
      answer = clf.predict(new_data)

Encoding the code means that it works with numbers in scikit-learn, and the strings must be converted into code, which will be done using the following library:

     le = preprocessing.LabelEncoder()
     le.fit(Symbol)
     df['Name label'] = le.transform(Symbol)
     Name_label=df['Name label']

To search for a value in the columns of the data set, we use the following code:

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

This code gives the number of answers requested:

    for i in range(len(new_data)):
          df_name=df[df['Name label']==answer[i]]
          search_name = df_name['Symbol Coin'].tolist()
          print(f'Cryptocurrency price your number {i+1} choice ====> {search_name[0]}')

Data frame columns can be created using a dictionary:

   dic={'Symbol Coin':symbol,'Name Coin':name,'NameId':nameid,'Rank Coin':rank,'Price Coin':price,'Percent Change 24h':percent_change_24h,
     'Percent Change 1h':percent_change_1h,'Percent Change 7d':percent_change_7d,'Market Cap USD':market_cap_usd,'Volume':volume24}
   df=pd.DataFrame(dic)
