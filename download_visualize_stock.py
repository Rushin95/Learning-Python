# Download stock info from Yahoo finance and visualize the closing stock

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

def fetch_stock():
    start_date = dt.datetime(2016,11,1)
    end_date = dt.datetime(2017,11,12)
    df = web.DataReader('AMZN','yahoo',start_date,end_date)
    print(df.head(10))
    style.use('ggplot')
    df['Close'].plot()
    plt.title('Closing Stocks of Amazon between '+str(start_date.strftime("%B %d, %Y"))+' and '+str(end_date.strftime("%B %d, %Y")))
    plt.ylabel('Closing Stock')
    plt.xlabel('Date')
    plt.show()

fetch_stock()
