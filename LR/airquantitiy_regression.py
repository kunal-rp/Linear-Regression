
# Code source: Jaques Grobler
# License: BSD 3 clause

import pandas as pd # conventional alias
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('AirQualityUCI.csv')



print(df.isnull().values.any())

plt.scatter(df['Time'],df['T'])
plt.show()
