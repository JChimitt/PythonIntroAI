# classify handwritten digits using small set of 1797 handwritten digits.

import numpy as np
import matplotlib.pyplot as plt
#from sklearn.datasets import fetch_openml
from sklearn.datasets import load_digits

# 1797 handwritten digits
digits_ds = load_digits()
X = digits_ds['data']
Y = digits_ds['target']
print(X.dtype, Y.dtype)
print(X.shape, Y.shape)

# plot. digits data is a 3D array each consisting of 8x8 grid of pixels
# plot 10 rows and 10 cols of digits.
fig, axes = plt.subplots(5,4, figsize=(8,8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits_ds.images[i], cmap='binary', interpolation = 'nearest')
    ax.text(0.05,0.05, str(digits_ds.target[i]),
            transform=ax.transAxes, color='green')


#p = np.random.permutation(len(X))
#p = p[:20] 

# split data into training and test sets
from sklearn.model_selection import train_test_split
train_X, test_X, train_Y, test_Y = train_test_split(X, Y)

# Use Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
cls = MultinomialNB()
cls.fit(train_X, train_Y)

# score
print(cls.score(test_X, test_Y))

# How well did it classif each digit 0-9
from sklearn.metrics import classification_report
predictions = cls.predict(test_X)
print("\nClassification Results using Naive-Bayes Classifier\n")
print(classification_report(test_Y, predictions))

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(train_X, train_Y)
# score
print(clf.score(test_X, test_Y))

predictions = clf.predict(test_X)
print("\nClassification Results using Decision Tree Classifier\n")
print(classification_report(test_Y, predictions))






