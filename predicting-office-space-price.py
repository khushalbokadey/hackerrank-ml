#!/usr/bin/python

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

line = raw_input()

f = int(line.split(' ')[0])
h = int(line.split(' ')[1])

X_train = []
X_label = []

for i in range(0, h):
	line = raw_input()
	feature_list = [float(x) for x in line.split(' ')]
	X_label.append(feature_list[-1])
	feature_list.pop()
	X_train.append(feature_list)

line = raw_input()
t = int(line)

X_test = []

for i in range(0, t):
	line = raw_input()
	feature_list = [float(x) for x in line.split(' ')]
	X_test.append(feature_list)


poly = PolynomialFeatures(degree=f+1)
X_ = poly.fit_transform(X_train)
predict_ = poly.fit_transform(X_test)

clf = linear_model.LinearRegression()
clf.fit(X_, X_label)
pred = clf.predict(predict_)

for i in range(0, len(pred)):
	print pred[i]