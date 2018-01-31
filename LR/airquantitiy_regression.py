
# Code source: Jaques Grobler
# License: BSD 3 clause

import pandas as pd # conventional alias
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('GOOGL.csv')



xs = (df['Close'] - df['Open'])/df['Close'] * 100
ys = df['Volume']


def generate(size, cor, dif):
    X = []
    Y = []
    for x in range(0,size):
        X.append(x)
        if(cor):





#returns the mean of a list
def mean(a):
    return np.mean(a)

#Returns the best fit slope
def get_BTSlope(xs, ys):

    m = (mean(xs) * mean(ys) - mean(xs * ys)) / (mean(xs)**2 - mean(xs**2))

    return m

def get_YInter(xs, ys, m):

    return mean(ys) - m*mean(xs)


def predict(x, m, b):
    return m*x + b

def squared_error(orig,calc):
    return sum((calc - orig)**2)

def coef_determination(orig, calc):
    y_mean = [mean(orig) for y in orig]
    print("Y")
    squared_error_reg = squared_error(orig, calc)
    squared_error_mean = squared_error(orig, y_mean)
    return 1-squared_error_reg/squared_error_mean

print(mean(xs))
print(mean(ys))


m = get_BTSlope(xs, ys)
b = get_YInter(xs, ys, m)
regression_line = [predict(x,m,b) for x in xs]

r = coef_determination(ys, regression_line)
#Coefficient of 1 is the best accuracy
print("r2 : ", r)

#print("Predict at time 4: ", predict(4,m,b))

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()
