from statistics import mean
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6],dtype = np.float64)
ys = np.array([5,4,5,6,7,6],dtype = np.float64)

print(xs * ys)




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

m = get_BTSlope(xs, ys)
b = get_YInter(xs, ys, m)

regression_line = [predict(x,m,b) for x in xs]


r = coef_determination(ys, regression_line)

#Coefficient of 1 is the best accuracy
print("r2 : ", r)

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()
