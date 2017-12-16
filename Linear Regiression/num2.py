
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('sample.txt')
y_values = dataframe[['y']]
print(y_values.length)
x1_values = dataframe[['x1']]
x2_values = dataframe[['x2']]
x3_values = dataframe[['x3']]
x4_values = dataframe[['x4']]
x5_values = dataframe[['x5']]
x6_values = dataframe[['x6']]
x7_values = dataframe[['x7']]
print(x7_values)

#train model on data
body_reg = linear_model.LinearRegression()
x_values = [x1_values,x2_values,x3_values,x4_values,x5_values,x6_values,x7_values]
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
