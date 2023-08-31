
![Bitcoin-Cryptocurrency-Placeholder](https://github.com/Peyman2012/Cryptocurrency-price-with-Scikit-learn/assets/88220773/f84ff9d4-d663-45c9-8cce-1ee23e26f02f)

**Cryptocurrency-price-with-Scikit-learn**

We cannot use classification in this project because the classifier generally separates distinct classes, and so this classifier expects a string or an integer type to distinguish different classes from each other (this is called the "target " Is known). You can read more about this in Introduction to Classifiers.

The problem we are trying to solve is to determine a continuous numerical output, Result. This is known as a regression problem, so we need to use a regression algorithm (such as DecisionTreeRegressor).

      clf = tree.DecisionTreeClassifier()
      clf = clf.fit(x, y)
      new_data = [['2392999', '2350104.0', '2402000.0', '2371496.0'], ['46.7296', '45.5101', '47.0', '45.5267'], ['150000', '147000.1', '151400.0', '148998.9']]
      answer = clf.predict(new_data)

Encoding the code means that it works with numbers in scikit-learn, and the strings must be converted into code, which will be done using the following library:
     le = preprocessing.LabelEncoder()
     le.fit(Symbol)
     df['Name label'] = le.transform(Symbol)
     Name_label=df['Name label']

To search for a value in the columns of the data set, we use the following code:
    for i in range(len(d_data)):
    symbol.append(d_data[i]['baseAsset'])
    open_price.append(d_data[i]['openPrice'])
    low_price.append(d_data[i]['lowPrice'])
    high_price.append(d_data[i]['highPrice'])
    bid_price.append(d_data[i]['bidPrice'])
    ask_price.append(d_data[i]['askPrice'])
    last_price.append(d_data[i]['lastPrice'])
    volume.append(d_data[i]['volume'])

