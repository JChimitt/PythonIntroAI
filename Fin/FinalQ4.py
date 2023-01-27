# Linear regression with multiple independent variables.

import pandas as pd
import numpy as np

# import all data into dataframe.
# - Temperature (AT) in the range 1.81°C and 37.11°C,
# - Ambient Pressure (AP) in the range 992.89-1033.30 milibar,
# - Relative Humidity (RH) in the range 25.56% to 100.16%
# - Exhaust Vacuum (V) in teh range 25.36-81.56 cm Hg
# - Net hourly electrical energy output (PE) 420.26-495.76 MW

data_df = pd.read_csv('Real estate valuation data set.csv')
# print out top five recs.
#print(data_df.head())

# Extract first four columns as the independent variables
# Extract last columns as dependent variable.
X = data_df.drop(['No', 'X6', 'Y'], axis=1).values
y = data_df.drop(['X1','X2','X3','X4','X5'], axis=1).values
#print("X=\n",X)
#print("y=\n",y)

# split data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    random_state=0)

from sklearn.neural_network import MLPRegressor
mlp = MLPRegressor(hidden_layer_sizes=(100,100),
                   activation='relu',
                   solver='adam',
                   learning_rate_init=.001,
                   n_iter_no_change=300)
# Train the NN
mlp.fit(X_train, y_train)

# Predict on the test set
predictions = mlp.predict(X_test)
print(predictions[:50])


from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

print("\nMean squared error =", mean_squared_error(y_test,predictions))
print("\nMean absolute error =", mean_absolute_error(y_test,predictions))
print("\n")
