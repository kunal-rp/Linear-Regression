#model the data with linear regression
import pandas as pd
import math
import datetime
import time
import numpy as np
from sklearn import preprocessing, cross_validation, svm #support vector machine for regression
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv('GOOGL.csv')
df['HLC'] = (df['High'] - df['Low'])/df['Low'] * 100.0
df['PCT_CHG'] = (df['Close'] - df['Open'])/df['Open'] * 100.0
df = df[['Close','HLC','PCT_CHG','Volume']]

forcast_col = 'Close'
print("Num of Days: ",len(df))

# This is the number of days ahead we are trying to guess the 'Close' price ; i.e. - for 20 days and 10%, we are guessing for two days ahead of today
forcast_out = int(math.ceil(0.01*len(df)))
print("Num of Days Out: ",forcast_out)

#Shifting the rows up by the # of days and filling in all NAN
df['label'] = df[forcast_col].shift(-forcast_out)
#instead of repacing all NAN with -999999, We remove those rows so that they don't interfere with prediction




#Gets the values between -1 and 1 to help with calculations
#In future, when we add realtime data, we have to rescale with the training + new data
X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forcast_out:]
X = X[:-forcast_out:]

df.dropna(inplace=True)
Y = np.array(df['label'])



X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X,Y,test_size = .02)

clf = LinearRegression()
clf.fit(X_train, Y_train)
confidence = clf.score(X_test, Y_test)
forcast_set = clf.predict(X_lately)
print(confidence,forcast_set,forcast_out)
df['Forcast'] = np.nan

last_date = df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple())
#last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forcast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1 + i)]

df['Close'].plot()
df['Forcast'].plot()

plt.legend(loc=4)
