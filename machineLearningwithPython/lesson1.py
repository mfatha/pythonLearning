'''
    ===========================================================
    ========================REGRESSION=========================
    ===========================================================
'''
#import pandas and quandl library
import pandas as pd
import quandl as ql
import math

#quandl fetch data from Url
df = ql.get('WIKI/GOOGL')

#required Columns
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#high- low percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
#percentage change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forcast_col = 'Adj. Close'
#replace null values in data Frame
df.fillna(-99999, inplace =True)

#forcasting
forcast_out = int(math.ceil(0.01*len(df)))

#adding forcast data to Label
df['label'] = df[forcast_col].shift(-forcast_out)
df.dropna(inplace=True)

print(df.head())
