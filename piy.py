

import datetime as dt
import json
import time
from time import sleep

import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import requests
import schedule

key = "https://api.binance.com/api/v3/ticker/price?"
data = requests.get(key)  
data = data.json()

df = pd.DataFrame(data)

df.plot()












         