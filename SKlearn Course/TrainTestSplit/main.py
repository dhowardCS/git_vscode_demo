from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
#split into features and labels
X = iris.data
y = iris.target

print(X.shape)
print(y.shape)

#hours of study vs good/bad grades
#10 different students, train with 8, predict with last 2
#allows for determining model accuracy 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2 )
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)