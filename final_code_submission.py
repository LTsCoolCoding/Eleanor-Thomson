from calendar import month
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

# Set date range; we wanted to pull data from the last 10 years
start_date = '2010-01-01'
end_date = '2024-12-31'

# Download all available data; this is where we actually pulled the data into a new data set 'data'
data = yf.download(list(tickers.values()), start=start_date, end=end_date)

# We then exported 'data' our df to a csv using the .to_csv function
data.to_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\data_return.csv')

#Made manual adjustments on exported file and created new CSV with close data called "close_data_final"
#The reason we had to make manual edits on the cvs was to fix formatting of the export,
# and the columns were messed up - the edits made were removing indexes high, low, and volume traded
# as well as removing unnecessary blank rows *insert image in actual presentation*

# Reading new csv file
df1 = pd.read_csv("C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\close_data_final.csv")

#Turn Dates to a datetime data type
df1['Date'] = pd.to_datetime(df1['Date'])

#Sort data
df1_sorted = df1.sort_values('Date')

#Implement a forward fill to capture values in days where market closed (primarily Sat & Sun)
df1_sorted.ffill(axis = 0, inplace = True)

df1_sorted.to_csv("C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\df1_filled.csv", index = False)

##CHECK POINT


#Now lets calculate monthly returns using the 1st of every month

#First lets turn the Date column to our index
df1_sorted.set_index('Date', inplace=True)

#Take the first of every month
first_of_month_df = df1_sorted[df1_sorted.index.day == 1]

first_of_month_df.to_csv("C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\first_of_m.csv")



#Calculate Returns
monthly_returns = first_of_month_df.pct_change()

monthly_returns.to_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\monthly_returns.csv')


#############################################################################################################


### Reading M2 csv downloaded straight from FRED ###
M2 = pd.read_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\M2SL.csv')

### Reading establishment(CES) employment stats ###
ces = pd.read_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\total_employment_nonfarm.csv')

### Reading household surveys for employment ###
house_emp = pd.read_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\employment_level.csv')

returns = pd.read_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\monthly_returns.csv')

#For a better layout, lets sort based on year for both datasets

melted_house = pd.melt(house_emp, id_vars=["Year"], var_name="Month", value_name="Employment")
melted_establishment = pd.melt(ces, id_vars=["Year"], var_name="Month", value_name="Nonfarm_Employment")

#For a better layout, lets sort based on year for both datasets
house_sorted = melted_house.sort_values('Year')
est_sorted = melted_establishment.sort_values('Year')

month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']

house_sorted['Month'] = pd.Categorical(house_sorted['Month'], categories=month_order, ordered=True)
house_sorted.sort_values(by=['Year','Month'], inplace=True)

est_sorted['Month'] = pd.Categorical(est_sorted['Month'], categories=month_order, ordered=True)
est_sorted.sort_values(by=['Year','Month'], inplace=True)

house_sorted.to_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\house_sorted.csv')
est_sorted.to_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\est_sorted.csv')

house_sorted['Date'] = house_sorted['Month'].astype(str) + ' ' + house_sorted['Year'].astype(str)
est_sorted['Date'] = est_sorted['Month'].astype(str) + ' ' + est_sorted['Year'].astype(str)
house_sorted = house_sorted.drop(columns = ['Month','Year'])
est_sorted = est_sorted.drop(columns = ['Month','Year'])

emp_final = house_sorted.merge(est_sorted, how = 'inner', on = 'Date')
cols = ['Date'] + [col for col in emp_final.columns if col != 'Date']
emp_final = emp_final[cols]

M2['observation_date'] = pd.to_datetime(M2['observation_date'])

M2['observation_date'] = M2['observation_date'].dt.strftime('%b %Y')
M2 = M2.rename(columns={'observation_date': 'Date'})
emp_M2 = emp_final.merge(M2, how = 'inner', on = 'Date')

emp_M2['Date'] = pd.to_datetime(emp_M2['Date'])
emp_M2.to_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\emp_M2.csv')

returns['Date'] = pd.to_datetime(returns['Date'])

final_data = emp_M2.merge(returns, how = 'inner', on = 'Date')
final_data.to_csv('C:\\Users\\esteb\\Documents\\School\\Business_Intelligence\\Project\\final_data.csv')