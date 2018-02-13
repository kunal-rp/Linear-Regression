from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn import model_selection as ms
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv');

x = []
y = []


for index, row in df.iterrows():
    #,row['SepalWidthCm'],row['PetalLengthCm'],row['PetalWidthCm']

    '''
    I am changing the attibutes appended to the x data to see how to better the confidence in both models
    '''
    x.append([row['PetalWidthCm'],row['PetalLengthCm']])
    if row['Species'] == 'Iris-setosa':
        y = np.append(y,[0])
    elif row['Species'] == 'Iris-versicolor':
        y = np.append(y,[1])
    else:
        y = np.append(y,[2])



x = np.array(x)
y = np.array(y)
X_train, X_test, Y_train, Y_test = ms.train_test_split(x,y,test_size = .02)

clf1 = LinearRegression()
clf2 = GaussianNB()


clf1.fit(X_train,Y_train)
clf2.fit(X_train,Y_train)
print("Linear Regression :",clf1.score(X_test, Y_test))
print("Guassian NB  :",clf2.score(X_test, Y_test))
