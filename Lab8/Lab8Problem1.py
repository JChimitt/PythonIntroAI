# Linear regression with multiple independent variables.

import pandas as pd
import numpy as np

# import all data into dataframe.
# - Temperature (AT) in the range 1.81°C and 37.11°C,
# - Ambient Pressure (AP) in the range 992.89-1033.30 milibar,
# - Relative Humidity (RH) in the range 25.56% to 100.16%
# - Exhaust Vacuum (V) in teh range 25.36-81.56 cm Hg
# - Net hourly electrical energy output (PE) 420.26-495.76 MW

data_df = pd.read_csv('data-Lab10.csv')
# print out top five recs.
#print(data_df.head())

# Extract first four columns as the independent variables
# Extract last columns as dependent variable.
X = data_df.drop(['Tar', 'Gas', 'Char', 'Out_T'], axis=1).values
y = data_df['Out_T'].values
#print("X=\n",X)
#print("y=\n",y)

# split data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=0)

from sklearn import linear_model
clf = linear_model.Lasso(alpha=0.29)

# Train the NN
clf.fit(X_train, y_train)

# Predict on the test set
predictions = clf.predict(X_test)
print(predictions[:50])


from sklearn.metrics import mean_squared_error

print("\nMean squared error =", mean_squared_error(y_test,predictions))
print("\n")

pred_y_df = pd.DataFrame({'Actual Value': y_test, 
                          'Predicted Value': predictions, 
                          'Difference': y_test - predictions})
print(pred_y_df[0:20])