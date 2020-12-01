# Program to measure the similarity between
# two sentences using cosine similarity.
import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from csv import reader
from flask import jsonify


def similarity_score(X, Y, sw):
	# tokenization
	X_list = word_tokenize(X.lower())
	Y_list = word_tokenize(Y.lower())

	# remove stop words from the string
	X_set = {w for w in X_list if not w in sw}
	Y_set = {w for w in Y_list if not w in sw}
	l1 =[];l2 =[]

	# form a set containing keywords of both strings
	rvector = X_set.union(Y_set)
	for w in rvector:
		if w in X_set: l1.append(1) # create a vector
		else: l1.append(0)
		if w in Y_set: l2.append(1)
		else: l2.append(0)
	c = 0

	# cosine formula
	for i in range(len(rvector)):
			c+= l1[i]*l2[i]
	cosine = c / float((sum(l1)*sum(l2))**0.5)
	return cosine

def link_and_label(filename, input_text, sw):
	# open file in read mode
	with open(filename, "r", encoding = 'utf-8') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		titles = []
		links = []
		labels = []
		for lines in csv_reader:
			titles.append(lines['Title'])
			links.append(lines['Link'])
			labels.append(lines['Label'])

		max_score = 0.0
		title = " "
		link = " "
		label = " "
		for i in range(len(titles)):
			score = similarity_score(input_text, titles[i], sw)
			if(score > max_score):
				max_score = score
				title = titles[i]
				link = links[i]
				label = labels[i]
		if(max_score > 0.97):
			data = {"title": "Matched Search : " + title,
			"score": "Matching percentage: " + str(round( max_score*100, 2)) + "%",
			"link": "For complete fact checking refer this link: " + link,
			"label": "Intensity of lie: " + str(label)}
			return jsonify(data)
		elif(max_score > 0.5 and max_score < 0.97):
			data = {"title": "Matched Search : " + title,
			"score": "Matching percentage: " + str(round( max_score*100, 2)) + "%",
			"link": "For complete fact checking refer this link: " + link,
			"label": "Intensity of lie: " + str(label)}
			return jsonify(data)
		else:
			data = {"label" : "This news doesn't exist in our dataset"}
			return jsonify(data)

def predict(input_text):

	# nw contains list of negation worldsnw
	nw = ["n't", "no", "not", "none", "nobody", "nothing", "neither", "nowhere", "never"]
	negation_words = set(nw)
	stop_words = set(stopwords.words('english')) - negation_words

	# sw contains the list of stopwords
	sw = list(stop_words)
	return link_and_label('Fake_News_Dataset.csv', input_text, sw)
