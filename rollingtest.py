#PYTHON FOR FINANCE: RISK & RETURN

# https://pythonprogramming.net/ - source with projects, examples 
# tutorial source: video 1: https://www.youtube.com/watch?v=zoyzoNClXE4&list=PLvMRWNpDTNwRAriwbJLNymcSDN-Rw_pv_ 
# source video 2: (ATR) https://www.youtube.com/watch?v=ZpI-JDfuCs4&list=PLvMRWNpDTNwRAriwbJLNymcSDN-Rw_pv_&index=2



import numpy as np
import pandas_datareader as pdr 
import datetime as dt 
import pandas as pd 
import matplotlib.pyplot as plt


#getting data from API with pdr - pandas datareader

tickers = ['TSLA']
start = dt.datetime(2020, 1,1)
data = pdr.get_data_stooq(tickers, start)


#applying volatility formula to data pulled


#ATR below
#true range ---> TR = max[ H - L, |H-C_p|, |L - C_p| ]
#ATR is sum:TR over n, where n is a time interval


#  I   ----   from thre data pulled above, define elements of the true range and ATR formula
high_low = data['High'] - data['Low']


#  II  ----   numpy function for abs value, shift takes the previous value(close)
high_cp = np.abs(data['High'] - data['Close'].shift())


#  III ----   third expression from TR formula - true range
low_cp = np.abs(data['Low'] - data['Close'].shift())


#   ----  df - dataframe used to (__??___) organize the data?? for the calcuation of true range using all expressions in the formula
df = pd.concat([high_low, high_cp, low_cp], axis=1)

#  IV  ----- calculating true range
true_range = np.max(df, axis=1)


#  V ----- ATR - average true range  --rolling() determines how many values/data points are used for calculations
average_true_range = true_range.rolling(14).mean()





#--- Plotting the data with matplotlib #--- Plotting the data with matplotlib #--- Plotting the data with matplotlib  #--- Plotting the data with matplotlib

#subplot()???
fig, ax = plt.subplots()
average_true_range.plot(ax=ax)

##for generating visual plot
#plt.show()

#adding another value - 'Close' values to the plot
#alpha parameter scales the x axis on the right side 
ax2 = data['Close'].plot(ax=ax, secondary_y=True, alpha=.3)
ax.set_ylabel("ATR")
ax2.set_ylabel("Price")


##for generating visual plot
plt.show()
#reports data -head(n) begins from date to nth, #tail(), 
data.head()
