from pybit import HTTP
import pandas as pd
import numpy as np
import datetime
import time
import os

#download kline data for daily candle for btcusd
session = HTTP("https://api.bybit.com")
#define variable for time now in epoch time
now = int(time.time())
#define variable for time 1 day ago in epoch time
yesterday = now - (86400 * 1000)
#define variable for time 30 minutes ago in epoch time
thirtymin = now - (30 * 60 * 1000)



while yesterday < thirtymin:
    data = session.query_kline(
        symbol="BTCUSD",
        interval="15",
        from_time=yesterday
    )
    volume = data['result'][-1]['volume']
    time_now = data['time_now']
    datalookback = 199
    historical_volume = pd.DataFrame(data['result'][-datalookback:])
    volume30d = historical_volume['volume']
    time_now30d = historical_volume['open_time']
    volumedata30d = pd.DataFrame({'volume30d': volume30d, 'time_now30d': time_now30d})
    volumedata30d.rename(columns={'time_now30d': 'time','volume30d': 'volume', }, inplace=True)
    volumedata30d.set_index('time', inplace=True)
    print(volumedata30d)
    #grab the last time in the dataframe
    last_time = volumedata30d.index[-1]
    yesterday = last_time
    #if historical volume.csv exists, append new data to it
    if os.path.isfile('historical_volume.csv'):
        volumedata30d.to_csv('historical_volume.csv', mode='a', header=False)
    #if historical volume.csv does not exist, create it
    else:
        volumedata30d.to_csv('historical_volume.csv')
    time.sleep(3)
else:
    print("done")






