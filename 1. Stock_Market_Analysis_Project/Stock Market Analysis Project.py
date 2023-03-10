#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# <center>*Copyright Pierian Data 2017*</center>
# <center>*For more information, visit us at www.pieriandata.com*</center>

# # Stock Market Analysis Project
# 
# ### Please Note: You are free to treat this as a full exercise, or just view the solutions video as a code along project. This project is meant to be pretty challenging as it will introduce a few new concepts through some hints!
# 
# Welcome to your first capstone project! This project is meant to cap off the first half of the course, which mainly dealt with learning the libraries that we use in this course, the second half of the course will deal a lot more with quantitative trading techniques and platforms.
# 
# We'll be analyzing stock data related to a few car companies, from Jan 1 2012 to Jan 1 2017. Keep in mind that this project is mainly just to practice your skills with matplotlib, pandas, and numpy. Don't infer financial trading advice from the analysis we do here!
# 
# ### Part 0: Import
# 
# ** Import the various libraries you will need-you can always just come back up here or import as you go along :) **

# In[106]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import datetime


# ____
# ## Part 1: Getting the Data
# 
# ### Tesla Stock (Ticker: TSLA on the NASDAQ)
# 
# **  *Note! Not everyone will be working on a computer that will give them open access to download the stock information using pandas_datareader (firewalls, admin permissions, etc...). Because of this, the csv file for the Tesla is provided in a data folder inside this folder. It is called Tesla_Stock.csv. Feel free to just use this with read_csv! **
# 
# ** Use pandas_datareader to obtain the historical stock information for Tesla from Jan 1, 2012 to Jan 1, 2017.**
# 
# 

# In[ ]:





# In[ ]:





# In[107]:


#Tesla
Tesla_data = pd.read_csv('Tesla_Stock.csv')
Tesla_data = Tesla_data.set_index('Date')
Tesla = Tesla_data.loc['2012-01-01': '2017-01-01']
Tesla.head()


# In[77]:





# In[ ]:





# ### Other Car Companies
# 
# ** Repeat the same steps to grab data for Ford and GM (General Motors), **

# In[108]:


#Ford Data
Ford_data = pd.read_csv('Ford_Stock.csv')
Ford_data = Ford_data.set_index('Date')
Ford = Ford_data.loc['2012-01-01': '2017-01-01']

Ford.head()


# In[ ]:





# In[ ]:





# In[109]:


#GM
GM_data = pd.read_csv('GM_Stock.csv')
GM_data = GM_data.set_index('Date')
GM = GM_data.loc['2012-01-01': '2017-01-01']
GM.head()


# In[ ]:





# In[ ]:





# ## Part 2: Visualizing the Data
# 
# ** Time to visualize the data. **
# 
# ** Follow along and recreate the plots below according to the instructions and explanations. **

# ____
# 
# ** Recreate this linear plot of all the stocks' Open price ! Hint: For the legend, use label parameter and plt.legend()**

# In[110]:


Tesla['Open'].plot(label='Tesla',figsize=(16,8),title='Opening Prices')
GM['Open'].plot(label='GM')
Ford['Open'].plot(label='Ford')

plt.legend()
plt.show()


# In[ ]:





# ____

# ** Plot the Volume of stock traded each day.**

# In[111]:


Tesla['Volume'].plot(label='Tesla',figsize=(16,8),title='Volume Traded')
GM['Volume'].plot(label='GM')
Ford['Volume'].plot(label='Ford')

plt.legend()
plt.show()


# ** Interesting, looks like Ford had a really big spike somewhere in late 2013. What was the date of this maximum trading volume for Ford?**
# 
# **Bonus: What happened that day? **

# In[ ]:





# In[112]:


Ford[Ford['Volume']==Ford['Volume'].max()]
    


# ____

# ** The Open Price Time Series Visualization makes Tesla look like its always been much more valuable as a company than GM and Ford. But to really understand this we would need to look at the total market cap of the company, not just the stock price. Unfortunately our current data doesn't have that information of total units of stock present. But what we can do as a simple calcualtion to try to represent total money traded would be to multply the Volume column by the Open price. Remember that this still isn't the actual Market Cap, its just a visual representation of the total amount of money being traded around using the time series. (e.g. 100 units of stock at \$10 each versus 100000 units of stock at $1 each)**

# ** Create a new column for each dataframe called "Total Traded" which is the Open Price multiplied by the Volume Traded.**

# In[113]:


# Code Here 
pd.options.mode.chained_assignment = None
Tesla['Total Traded'] = (Tesla['Open'])*(Tesla['Volume'])
Ford['Total Traded'] = (Ford['Open'])*(Ford['Volume'])
GM['Total Traded'] = (GM['Open'])*(GM['Volume'])


# In[114]:


Ford.head()


# ** Plot this "Total Traded" against the time index.**

# In[115]:


Tesla['Total Traded'].plot(label='Tesla',figsize=(16,8),title='Total Traded')
GM['Total Traded'].plot(label='GM')
Ford['Total Traded'].plot(label='Ford')

plt.legend()
plt.show()


# In[ ]:





# ** Interesting, looks like there was huge amount of money traded for Tesla somewhere in early 2014. What date was that and what happened? **

# In[ ]:





# In[15]:


Tesla[Tesla['Total Traded']==Tesla['Total Traded'].max()]


# ____

# ** Let's practice plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for GM. **

# In[16]:


# Code here
GM['Open:50 Day Mean']=GM['Open'].rolling(50).mean()
GM['Open:200 Day Mean']=GM['Open'].rolling(200).mean()

GM['Open'].plot(label='GM',figsize=(16,8),title='Opening Price')
GM['Open:200 Day Mean'].plot(label='MA50')
GM['Open:50 Day Mean'].plot(label='MA200')

plt.legend()


# In[ ]:





# ______

# ** Finally lets see if there is a relationship between these stocks, after all, they are all related to the car industry. We can see this easily through a scatter matrix plot. Import scatter_matrix from pandas.plotting and use it to create a scatter matrix plot of all the stocks'opening price. You may need to rearrange the columns into a new single dataframe. Hints and info can be found here: https://pandas.pydata.org/pandas-docs/stable/visualization.html#scatter-matrix-plot **

# In[18]:


from pandas.plotting import scatter_matrix


# In[19]:


companies = pd.concat([Tesla['Open'],Ford['Open'],GM['Open']],axis=1)
companies.columns=['Tesla Open','Ford Open','GM Open']


# In[20]:


scatter_matrix(companies,figsize=(8,8),alpha=0.5,hist_kwds={'bins':50});


# In[ ]:





# _____
# ### Bonus Visualization Task! (Note: This is hard!)
# **Let's now create a candlestick chart! Watch the video if you get stuck on trying to recreate this visualization, there are quite a few steps involved!Refer to the video to understand how to interpret and read this chart. Hints: https://matplotlib.org/examples/pylab_examples/finance_demo.html**
# 
# ** Create a CandleStick chart for Ford in January 2012 (too many dates won't look good for a candlestick chart)**

# In[ ]:


#the hints are outdated and so i had to do a dive into the mplfinance documentation.
#https://github.com/matplotlib/mplfinance/wiki/Plotting-Too-Much-Data


# In[164]:


import mplfinance as mpf
import pandas as pd



# In[165]:



Ford_data = pd.read_csv('Ford_Stock.csv',index_col=0,parse_dates=True)
Ford_data.index.name = 'Date'

data = Ford_data.loc['2012-01-01':'2012-02-01']
mpf.plot(data,type='candle',style='yahoo')


# In[ ]:





# In[ ]:





# In[ ]:





# ____
# # Part 3: Basic Financial Analysis
# 
# Now it is time to focus on a few key financial calculations. This will serve as your transition to the second half of the course. All you need to do is follow along with the instructions, this will mainly be an exercise in converting a mathematical equation or concept into code using python and pandas, something we will do often when working with quantiative data! If you feel very lost in this section, don't worry! Just go to the solutions lecture and treat it as a code-along lecture, use whatever style of learning works best for you!
# 
# Let's begin!
# ____

# ## Daily Percentage Change
# First we will begin by calculating the daily percentage change. Daily percentage change is defined by the following formula:

# $ r_t = \frac{p_t}{p_{t-1}} -1$

# This defines r_t (return at time t) as equal to the price at time t divided by the price at time t-1 (the previous day) minus 1. Basically this just informs you of your percent gain (or loss) if you bought the stock on day and then sold it the next day. While this isn't necessarily helpful for attempting to predict future values of the stock, its very helpful in analyzing the volatility of the stock. If daily returns have a wide distribution, the stock is more volatile from one day to the next. Let's calculate the percent returns and then plot them with a histogram, and decide which stock is the most stable!

# ** Create a new column for each dataframe called returns. This column will be calculated from the Close price column. There are two ways to do this, either a simple calculation using the .shift() method that follows the formula above, or you can also use pandas' built in pct_change method. **

# In[153]:


Ford['Returns'] = (Ford['Close'] / Ford['Close'].shift(1)) -1 


# In[154]:


Tesla['Returns'] = Tesla['Close'].pct_change(1)


# In[155]:


GM['Returns'] = GM['Close'].pct_change(1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ** Now plot a histogram of each companies returns. Either do them separately, or stack them on top of each other. Which stock is the most "volatile"? (as judged by the variance in the daily returns we will discuss volatility in a lot more detail in future lectures.)**

# In[156]:


Ford['Returns'].hist(bins=100)


# In[26]:


GM['Returns'].hist(bins=100)


# In[27]:


Tesla['Returns'].hist(bins=100)


# In[33]:


Ford['Returns'].hist(bins=100, label='Ford',figsize=(10,8),alpha = 1)
GM['Returns'].hist(bins=100,label='GM',figsize=(10,8),alpha = 0.5)
Tesla['Returns'].hist(bins=100, label='Tesla',figsize=(10,8),alpha=0.25)

plt.legend()


# ** Try also plotting a KDE instead of histograms for another view point. Which stock has the widest plot? **

# In[35]:


Ford['Returns'].plot(kind='kde', label='Ford',figsize=(10,8))
GM['Returns'].plot(kind='kde',label='GM',figsize=(10,8))
Tesla['Returns'].plot(kind='kde', label='Tesla',figsize=(10,8))

plt.legend()


# ** Try also creating some box plots comparing the returns. **

# In[38]:


box_df = pd.concat([Tesla['Returns'],Ford['Returns'],GM['Returns']],axis =1)
box_df.columns = ['Tesla Ret', 'Ford Ret', 'GM Ret']
box_df.plot(kind='box', figsize=(12,8))


# ## Comparing Daily Returns between Stocks
# 
# ** Create a scatter matrix plot to see the correlation between each of the stocks daily returns. This helps answer the questions of how related the car companies are. Is Tesla begin treated more as a technology company rather than a car company by the market?**

# In[39]:


scatter_matrix(box_df,figsize=(8,8),alpha=0.5,hist_kwds={'bins':100});


# 

# In[41]:


box_df.plot(kind='scatter', x='Ford Ret', y ='GM Ret',alpha=0.5,figsize=(8,8))


# ____
# ## Cumulative Daily Returns
# 
# Great! Now we can see which stock was the most wide ranging in daily returns (you should have realized it was Tesla, our original stock price plot should have also made that obvious).
# 
# With daily cumulative returns, the question we are trying to answer is the following, if I invested $1 in the company at the beginning of the time series, how much would is be worth today? This is different than just the stock price at the current day, because it will take into account the daily returns. Keep in mind, our simple calculation here won't take into account stocks that give back a dividend. Let's look at some simple examples:

# Lets us say there is a stock 'ABC' that is being actively traded on an exchange. ABC has the following prices corresponding to the dates given

#     Date                        Price
#     01/01/2018                   10
#     01/02/2018                   15
#     01/03/2018                   20
#     01/04/2018                   25

# **Daily Return** : Daily return is the profit/loss made by the stock compared to the previous day. (This is what ew just calculated above). A value above one indicates profit, similarly a value below one indicates loss. It is also expressed in percentage to convey the information better. (When expressed as percentage, if the value is above 0, the stock had give you profit else loss). So for the above example the daily returns would be

#     Date                         Daily Return                  %Daily Return
#     01/01/2018                 10/10 =  1                          -   
#     01/02/2018                 15/10 =  3/2                       50%
#     01/03/2018                 20/15 =  4/3                       33%
#     01/04/2018                 25/20 =  5/4                       20%

# **Cumulative Return**: While daily returns are useful, it doesn't give the investor a immediate insight into the gains he had made till date, especially if the stock is very volatile. Cumulative return is computed relative to the day investment is made.  If cumulative return is above one, you are making profits else you are in loss. So for the above example cumulative gains are as follows

#     Date                       Cumulative Return         %Cumulative Return
#     01/01/2018                  10/10 =  1                         100 %   
#     01/02/2018                  15/10 =  3/2                       150 %
#     01/03/2018                  20/10 =  2                         200 %
#     01/04/2018                  25/10 =  5/2                       250 %

# The formula for a cumulative daily return is:
# 
# $ i_i = (1+r_t) * i_{t-1} $
# 
# Here we can see we are just multiplying our previous investment at i at t-1 by 1+our percent returns. Pandas makes this very simple to calculate with its cumprod() method. Using something in the following manner:
# 
#     df[daily_cumulative_return] = ( 1 + df[pct_daily_return] ).cumprod()
#     

# ** Create a cumulative daily return column for each car company's dataframe.**

# In[44]:


Tesla['daily_cumulative_return'] = (1 + Tesla['Returns']).cumprod()
Ford['daily_cumulative_return'] = (1 + Ford['Returns']).cumprod()
GM['daily_cumulative_return'] = (1 + GM['Returns']).cumprod()


# In[47]:


GM.head()


# In[ ]:





# ** Now plot the Cumulative Return columns against the time series index. Which stock showed the highest return for a $1 invested? Which showed the lowest?**

# In[50]:


Tesla['daily_cumulative_return'].plot(label= 'Tesla', figsize=(16,8))
Ford['daily_cumulative_return'].plot(label= 'Ford', figsize=(16,8))
GM['daily_cumulative_return'].plot(label= 'GM', figsize=(16,8))

plt.legend()


# # Great Job!
# 
# That is it for thsi very basic analysis, this concludes this half of the course, which focuses much more on learning the tools of the trade. The second half of the course is where we really dive into functionality designed for time series, quantitative analysis, algorithmic trading, and much more!
