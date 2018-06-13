import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def calculateError(X,Y,m,b):

    total = sum( ( Y -  m * X + b) ** 2)
    return total

def runGradient(X,Y,m,b, learningRate):

    b_grad = 0
    m_grad = 0
    n = float(X.shape[0])
    for i in range(X.shape[0]):
        b_grad += -(2/n) * (Y[i] - ((m * X[i]) + b))
        m_grad += -(2/n) * X[i] * (Y[i] - ((m * X[i]) + b))
    new_b = (b - (learningRate * b_grad))
    new_m = (m - (learningRate * m_grad))
    return [new_b, new_m]

def runOptimization(X, Y):
    m = 1
    b = 1

    res = m*X + b
    plt.scatter(X,Y)
    plt.plot(X,res, color="red")
    plt.show()

    for i in range(1000):
        b,m = runGradient(X,Y,m,b, 0.0001)
        print "Error: ", calculateError(X,Y,m,b)

    res = m*X + b
    plt.scatter(X,Y)
    plt.plot(X,res, color="red")
    plt.show()
    
data = np.array(pd.read_csv('data.csv'))
X = data[:,0]
Y = data[:,1]
runOptimization(X,Y)
