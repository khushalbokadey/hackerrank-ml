#!/usr/bin/python

import json
import string
import unicodedata
import numpy as np

# from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# stopwords = set(stopwords.words('english'))

stopwords = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'o', 'hadn', 'herself', 'll', 'had', 'should', 'to', 'only', 'won', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'd', 'did', 'didn', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'hasn', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 're', 'does', 'above', 'between', 'mustn', 't', 'be', 'we', 'who', 'were', 'here', 'shouldn', 'hers', 'by', 'on', 'about', 'couldn', 'of', 'against', 's', 'isn', 'or', 'own', 'into', 'yourself', 'down', 'mightn', 'wasn', 'your', 'from', 'her', 'their', 'aren', 'there', 'been', 'whom', 'too', 'wouldn', 'themselves', 'weren', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'ma', 'these', 'up', 'will', 'below', 'ain', 'can', 'theirs', 'my', 'and', 've', 'then', 'is', 'am', 'it', 'doesn', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'yo', 'shan', 'needn', 'haven', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'm', 'yours', 'so', 'y', 'the', 'having', 'once']

# filePath = 'testcases/training-1.txt'
filePath = 'training.json'

def stopping(content):
	words = content.split()
	wordsFiltered = []
	for w in words:
		if w not in stopwords:
			wordsFiltered.append(w)

	newText = ' '.join(wordsFiltered)
	newText = newText.lstrip()
	return newText

def stemming(content):

	newText = ""
	if (len(content) > 1):

		### remove punctuation
		text_string = content.translate(string.maketrans("", ""), string.punctuation)
		text_string = " ".join(text_string.split())
		text_string = text_string.replace('\n', ' ')
		text_string = text_string.replace('\r', ' ')
		words = text_string.split(' ')

		### split the text string into individual words, stem each word,
		### and append the stemmed word to words (make sure there's a single
		### space between each stemmed word)

		stemmer = SnowballStemmer("english")

		words_after_stemming = []
		for i in range(0, len(words)):
			if (words[i] != ' '):
				words_after_stemming.append(stemmer.stem(words[i]).strip())

		newText = ' '.join(words_after_stemming)
		newText = newText.lstrip()

	return newText 

x_train = []
x_label = []
x_test = []

i=0

with open (filePath, "r") as inputFile:
	for line in inputFile:
		if (i != 0):
			data = json.loads(line)
			x_train.append(unicodedata.normalize('NFKD', data['question'] + " " + data['excerpt']).encode('ascii','ignore'))

			label = unicodedata.normalize('NFKD', data['topic']).encode('ascii','ignore').lower()
			x_label.append(label)

		i = i+1

line = raw_input()
n = int(line)

for i in range(0, n):
	line = raw_input()
	data = json.loads(line)
	x_test.append(unicodedata.normalize('NFKD', data['question'] + " " + data['excerpt']).encode('ascii','ignore'))

for i in range(0, len(x_train)):

	x_train[i] = x_train[i].lower()
	x_train[i] = stopping(x_train[i])
	# x_train[i] = stemming(x_train[i])


for i in range(0, len(x_test)):
	x_test[i] = x_test[i].lower()
	x_test[i] = stopping(x_test[i])
	# x_test[i] = stemming(x_test[i])


### Refer: http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(x_train)

from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, x_label)

X_new_counts = count_vect.transform(x_test)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for topic in predicted:
    print topic

actual_output = []

# with open ('testcases/output00.txt', "r") as output:
# 	for line in output:
# 		actual_output.append(line)

# for i in range(0, len(actual_output)):
# 	actual_output[i] = actual_output[i].replace('\n', '')

# print "Actual: "
# print actual_output

# accuracy = np.mean(predicted == actual_output)

# print "Accuracy: ", accuracy