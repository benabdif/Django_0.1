import datetime as dt
import json
import time
from time import sleep

import requests
import schedule
from numpy import intp

coin = input('Enter you CRYPTO: ').upper()
def mycoin(coin): 
    coinarry = ['BTC','XRP' ,'ETH', 'BNB']
    if coin in coinarry:
    # This link to make you get any one of the coin you need
        key = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
        #key = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"
        data = requests.get(key)  
        data = data.json()
        bicFadhel = f"{data['symbol']} price is {data['price']}"
        print(bicFadhel)
        
    else:
        print('Sorry you input no right...')
        
      
            
schedule.every(5).seconds.do(mycoin(coin))

while True:
    schedule.run_pending()
    time.sleep(2)
    

            
        


# def myfun(bicFadhel):
#     t = dt.datetime.now()
#     minut_count = 1000
#     while True:
#         delta_mintes = (dt.datetime.now() -t).seconds / 60
#         if delta_mintes and delta_mintes != minut_count:
#             print(bicFadhel)
#             minut_count = delta_mintes
#         sleep(1)
#         break
#     print(bicFadhel)
# myfun(bicFadhel)


#print(data)
#print(f"{data['symbol']} price is {data['price']}")
