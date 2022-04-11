import requests
import csv
import datetime

url='https://api.bybit.com/v2/public/kline/list'

price = requests.get(url + "?symbol=BTCUSD&interval=d&from=" + str(1617596700)).json()

csvheader = ['SYMBOL', 'TIME', 'CLOSE']
collector = []

#data filter
for x in price["result"] :
    pricing = [x['symbol'],x['open_time'],x['close'],]
    collector.append(pricing)


while int(float(collector[-1][1])) < 1649116800 :
    print(collector[-1][1])
    price = requests.get(url + "?symbol=BTCUSD&interval=d&from=" + str(collector[-1][1])).json()
    for x in price["result"] :
        pricing = [x['symbol'],x['open_time'],x['close'],]
        collector.append(pricing)
        print(collector[-1][1])
    with open('/Users/krow/downloads/dailyclose.csv', 'w', encoding = 'UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(collector)
else :
    print('finished')


