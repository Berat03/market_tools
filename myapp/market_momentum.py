import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def simple_moving_average(ticker_acc='MSFT', period='3mo', window = 5):
    ticker = yf.Ticker(ticker_acc)
    data = ticker.history(period)
    data = data[['Open']]
    data['MovingAverage'] = data['Open'].rolling(window=window, min_periods=None).mean()
    data = data.dropna()
    return data


dt = simple_moving_average()
dt.plot()
plt.show()