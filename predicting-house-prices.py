#!/usr/bin/python
from sklearn import linear_model

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

clf = linear_model.LinearRegression()
clf = clf.fit(X_train, X_label)

pred = clf.predict(X_test)

for i in range(0, len(pred)):
	print pred[i]