from readline import set_completion_display_matches_hook
import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import time
#function to request open intresset data from bybit api
def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data
#use the function to get the data for bitcoin open intresset
data = get_data('https://api.bybit.com/v2/public/tickers?symbols=BTCUSD')
#if open_intereset.csv exists, check if it has the time now header
if os.path.exists('open_interest.csv'):
    tf = pd.read_csv('open_interest.csv')
    if 'time_now' in tf.columns:
        pass
    else:
        #add delete the file
        os.remove('open_interest.csv')
else:
    #print ok
    print('ok')
#call the function every 10 seconds and store the time and open intereset in a csv file
while True:
    data = get_data('https://api.bybit.com/v2/public/tickers?symbols=BTCUSD')
    time_now = data["time_now"]
    open_interest = data["result"][0]["open_interest"]
    #create a dataframe with the time and open intereset
    df = pd.DataFrame({"time_now": [time_now], "open_interest": [open_interest]})
    #make time_now the index
    df = df.set_index("time_now")
    #append the last row of the dataframe to the csv file if it exists, if not create a new file
    if os.path.isfile('open_interest.csv'):
        df.to_csv('open_interest.csv', mode='a', header=False)
    else:
        df.to_csv('open_interest.csv')
    print(df.tail())
    #wait 10 seconds
    time.sleep(10)
########################################################################################################################



