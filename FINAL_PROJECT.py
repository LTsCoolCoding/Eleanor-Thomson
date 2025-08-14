#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:07:04 2025

@author: elthomson
"""
import yfinance as yf
import pandas as pd
import datetime as dt

# Define tickers for assets and make into a dictionary to pull from
tickers = {
    'S&P 500': '^GSPC',
    'DOW Jones': '^DJI',
    'NASDAQ': '^IXIC',
    'Gold (GLD)': 'GLD',
    'Oil (USO)': 'USO',
    'Bitcoin': 'BTC-USD'
}
############################################################### MEGNA
# Set date range; we wanted to pull data from the last 10 years
start_date = '2010-01-01'
end_date = '2024-12-31'

# Download all available data; this is where we actually pulled the data into a new data set 'data'
data = yf.download(list(tickers.values()), start=start_date, end=end_date)

# We then exported 'data' our df to a csv using the .to_csv function
data.to_csv('/Users/elthomson/Desktop/data_return.csv')
############################################################### JOSH 

#Made manual adjustments on exported file and created new CSV with close data called "close_data_final"
#The reason we had to make manual edits on the cvs was to fix formatting of the export,
# and the columns were messed up - the edits made were removing indexes high, low, and volume traded 
# as well as removing unnecessary blank rows *insert image in actual presentation*

# Reading new csv file
df1 = pd.read_csv(('/Users/elthomson/Desktop/BI/Final_Project/close_data_final.csv'))

#Turn Dates to a datetime data type
df1['Date'] = pd.to_datetime(df1['Date'])

#Sort data
df1_sorted = df1.sort_values('Date')

#Implement a forward fill to capture values in days where market closed (primarily Sat & Sun)
df1_sorted.ffill(axis = 0, inplace = True)

#put the new data thats been filled into a new file
df1_sorted.to_csv(('/Users/elthomson/Desktop/BI/Final_Project/df1_filled.csv'), index = False)


#Now lets calculate annual returns using Dec 31 as date of capture for
#First lets turn the Date column to our index
df1_sorted.set_index("Date", inplace=True)

#now lets change it to monthly data instead of daily- DATE CHANGE - using the first of each month as a refrernce

first_of_month_df=df1_sorted[df1_sorted.index.day==1]
first_of_month_df.to_csv('/Users/elthomson/Desktop/BI/Final_Project/dataforcosedata_firstdate.csv')



dec31_prices = df1_sorted[df1_sorted.index.strftime('%m-%d') == '12-31']

#To double check lets sort the dates
dec31_prices = dec31_prices.sort_index()

#Calculate Returns
monthly_returns = dec31_prices.pct_change()

monthly_returns.to_csv('/Users/elthomson/Desktop/BI/Final_Project/monthly_returns.csv')


##########################################################################$###################################
#Now lets gather some information on the M2 graph overtime

#Lets read the csv of M2 data we downloaded straight from FRED
m2 = pd.read_csv('/Users/elthomson/Desktop/BI/Final_Project/M2SL.csv')

#For employment data, only excel files were available. After some cleaning, turned into readable csv file

#Read establishment (CES) employment stats
ces = pd.read_csv('/Users/elthomson/Desktop/BI/Final_Project/total_employment_nonfarm.csv')

#Read household surveys for employment
house_emp = pd.read_csv('/Users/elthomson/Desktop/BI/Final_Project/employment_level.csv')

print(m2['observation_date'].dtype)
print(ces['Year'].dtype)
print(house_emp['Year'].dtype)





