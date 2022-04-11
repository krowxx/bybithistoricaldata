import requests
import csv
from pybit import HTTP

session = HTTP("https://api-testnet.bybit.com")

price = session.query_kline(
    symbol="BTCUSD",
    interval="1",
    from_time= 1617596700
)
csvheader = ['SYMBOL', 'TIME', 'CLOSE']
collector = []

#data filter
for x in price["result"] :
    pricing = [x['symbol'],x['open_time'],x['close'],]
    collector.append(pricing)

while collector[-1][1] < int(float(price['time_now'])) :
    price = session.query_kline(
        symbol="BTCUSD",
        interval="1",
        from_time= collector[-1][1]
    )
    for x in price["result"] :
        pricing = [x['symbol'],x['open_time'],x['close'],]
        collector.append(pricing)
        print(collector[-1][1])
    with open('priceoneyear.csv', 'w', encoding = 'UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(collector)
else :
    print('finished')






