# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:31:49 2015

@author: apple
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression




data=pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/data/ZYX_prices.csv')

feature_cols=['ZYX1MinSentiment','ZYX5minSentiment','ZYX10minSentiment','ZYX20minSentiment','ZYX30minSentiment','ZYX60minSentiment','ZYX60minTweets','ZYX30minTweets','ZYX20minTweets','ZYX10minTweets']
X = data[feature_cols]
y = np.where(data['60fret']>0, 1, 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
zip(feature_cols, logreg.coef_[0])

y_pred_class = logreg.predict(X_test)

print metrics.accuracy_score(y_test, y_pred_class)

prds = logreg.predict(X)
#sensitivity ie TRUE POSITIVES
print metrics.confusion_matrix(y_test, y_pred_class)
print metrics.confusion_matrix(y_test, y_pred_class)[1,1] / float(metrics.confusion_matrix(y_test, y_pred_class)[1,1] + metrics.confusion_matrix(y_test, y_pred_class)[1,0])
#specificity ie TRUE NEGATIVE
print metrics.confusion_matrix(y_test, y_pred_class)[0,0] / float(metrics.confusion_matrix(y_test, y_pred_class)[0,1] + metrics.confusion_matrix(y_test, y_pred_class)[0,0])