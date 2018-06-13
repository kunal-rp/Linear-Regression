#model the data with linear regression
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



df = pd.read_csv('GOOGL.csv')

df['HLC'] = (df['High'] - df['Low'])/df['Low'] * 100.0
df['PCT_CHG'] = (df['Close'] - df['Open'])/df['Open'] * 100.0
df = df[['Close','PCT_CHG','Volume']]

#X = np.array(df.drop(['Close','Volume'],1))
#Y = np.array(df.drop(['Volume','PCT_CHG'],1))
#Z = np.array(df.drop(['Close','PCT_CHG'],1))

X = [0,1,2,3,4,5,6,7,8,9]
Y = [0,0,0,0,0,0,0,0,0,0]
Z = [0,1,2,3,4,5,6,7,8,9]

test_in = [[10,11,12,13,14,15,16,17,18,19,20],[0,0,0,0,0,0,0,0,0,0]]
test_out = [10,11,12,13,14,15,16,17,18,19,20]

ax.scatter(X,Y,Z)
plt.show()
