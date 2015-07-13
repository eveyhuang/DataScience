
"""
Created on Wed Jul  8 20:45:16 2015

@author: Evey Huang
data from Kaggle Titanic: https://www.kaggle.com/c/titanic

Steps:
1. Read titanic.csv into a DataFrame.
2. Fill Age missing value with mean
3. Define Pclass, Parch, Age as the features, and Survived as the response.
4. Split the data into training and testing sets.
5. Fit a logistic regression model and examine the coefficients 
to confirm that they make intuitive sense.
6. Make predictions on the testing set and calculate the accuracy.
7. Create a confusion matrix and document the model's sensitivity and specificity. 

"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf

titanic=pd.read_csv('data/titanic.csv')
titanic.Age.fillna(titanic.Age.mean(), inplace=True)
feature_cols=['Pclass','Parch','Age']
X=titanic[feature_cols]
Y=titanic.Survived


X_train, X_test,Y_train, Y_test= train_test_split(X,Y,random_state=1)

from sklearn.linear_model import LogisticRegression
logreg= LogisticRegression()
logreg.fit(X_train, Y_train)
zip(feature_cols, logreg.coef_[0])

y_pred=logreg.predict(X_test)
print metrics.accuracy_score(Y_test, y_pred)

prds = logreg.predict(X)
print metrics.confusion_matrix(Y_test, y_pred)



