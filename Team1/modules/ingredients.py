from bs4 import BeautifulSoup
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
import re

word_tokenize = nltk.tokenize.TreebankWordTokenizer().tokenize

def get(recipe):
	ingredients = []
	for i in recipe.findAll("span",class_="recipe-ingred_txt"):
		words = word_tokenize(i.text)
		if len(words) < 1:
			continue;
		if words[0].lower() == "add":
			continue;

		ing = i.text
		ingredient = {}
		ingredient["name"] = getName(ing)
		ingredient["quantity"] = getQuantity(ing)
		ingredient["measurement"] = getMeasurement(ing)
		ingredient["preparation"] = getPreparation(ing)
		ingredient["descriptor"] = "none"
		ingredient["prep-description"] = "none"
		ingredients.append(ingredient)
	
	return ingredients

def getName(astring):
	names = []
	words = word_tokenize(astring)
	while isNum(words[0]):
		words.pop(0)
	for measurement in MEASUREMENTS:
		if measurement in words[0].lower():
			words.pop(0)
			break
	j = 0
	for word in words:
		if word in NAME_STOPWORDS:
			break
		j += 1
	words2 = words[:j]
	while words2[0][-2:] == "ed" and len(words2) > 1:
		words2.pop(0)

	if(len(words2) > 2):
		words2 = words2[-2:]
	return list2string(words2)

def getQuantity(astring):
	words = word_tokenize(astring)
	if isNum(words[0]):
		return words[0]
	return ""

def getMeasurement(astring):
	words = word_tokenize(astring)
	meas = []
	for word in words:
		for measurement in MEASUREMENTS:
			if measurement.lower() in word.lower():
				return word
	return "units"

def getPreparation(astring):
	words = word_tokenize(astring)
	preps = []
	for word in words:
		end = word[-2:]
		if end == "ed":
			return word
	return "none"



def isNum(astring):
	num_reg = re.compile('\d*([.,\/]?\d+)')
	isMatch = num_reg.match(astring)
	if isMatch:
		return True
	return False

def list2string(alist):
	return ' '.join(alist)

def unigrams(words):
	unis = []
	for word in words:
		if word[-2:] != "ed":
			unis.append(word)
	return unis


def bigrams(words):
	j = 0
	bis = []
	alen = len(words)
	while j < (alen - 1):
		bigram = [words[j],words[j+1]]
		bis.append(list2string(bigram))
	return bis


MEASUREMENTS = ['teaspoon','cup','tablespoon','pint','quart','gallon','pound','once','liter','pinch'];

NAME_STOPWORDS = [',','.']

# {
#     "name": ["olive oil"],
#     "quantity": [1],
#     "measurement": ["tablespoons", "tablespoon"],
#     "descriptor": [],
#     "preparation": [],
#     "prep-description": [],
#     "max": 3
# }
