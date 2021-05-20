import pandas as pd
from datetime import datetime
stock = pd.read_csv('sphist.csv')
stock['Date'] = pd.to_datetime(stock.Date)
stock["Date"] > datetime(year=2015, month=4, day=1)]
stock = stock.sort_values('Date', ascending=True)


