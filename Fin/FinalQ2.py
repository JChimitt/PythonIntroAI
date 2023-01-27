# Linear regression model using sklearn

import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Import data from sklearn toy dataset boston
iris_ds = load_iris()
#print(iris_ds)

# Convert imported dataset to a dataFrame.
df_X = pd.DataFrame(iris_ds.data, columns=iris_ds.feature_names)
#print(df_X)

# Create dataFrame for independent variable y.
df_Y = pd.DataFrame(iris_ds.target)
#print (df_Y)

df_Y.describe()

# Pick regression model
LR = linear_model.LinearRegression()


# Test size is 0.2 which implies 35% test size and Train set size is 65%
X_train, X_test, Y_train, Y_test = train_test_split(df_X, 
                                                     df_Y,
                                                     test_size=0.35,
                                                     random_state=4)

# Using Naives Bayes model to create model using train data
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, Y_train)
#print("Coefficients from model=\n",clf.coef_)

# Predict y values from input of x values
y_predicted = clf.predict(X_test)
#print("Predicted=\n",y_predicted)

from sklearn.metrics import accuracy_score
#print("First val in Predicted=",y_predicted[0])
#print("First val in y_test=",Y_test[0])
print("\nAccuracy Score=\n", accuracy_score(Y_test, y_predicted))
print("\n")

