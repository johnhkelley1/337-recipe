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
		ingredient["descriptor"] = getDescriptor(ing)
		ingredient["prep-description"] = getPrepDescription(ing)
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
		#if word in NAME_STOPWORDS:
			#break
		j += 1
	words2 = words[:j]
	while words2[0][-2:] == "ed" and len(words2) > 1:
		words2.pop(0)

	# if(len(words2) > 2):
	# 	words2 = words2[-2:]
	return list2string(words2)

def getQuantity(astring):
	words = astring.split()

	if isNum(words[1]) and isNum(words[0]):
		wh = words[0]
		num = float(wh)
		if("/" in words[1]):
			numer,den = words[1].split( '/' )
			num = float(wh) + float(numer)/float(den)
		return round(num,3)

	elif isNum(words[0]):
		num = words[0]
		if("/" in num):
			numer,den = num.split( '/' )
			num = float(numer)/float(den)
		num = float(num)
		return round(num,3)

	return "none"

def getMeasurement(astring):
	words = word_tokenize(astring)
	bis = bigrams(words)
	meas = []
	for word in words:
		for measurement in MEASUREMENTS:
			if measurement.lower() in word.lower():
				return word
	for bi in bis:
		if bi[0].lower() == 'to' and bi[1].lower() == 'taste':
			return 'to taste'
	return "units"

def getPreparation(astring):
	words = word_tokenize(astring)
	preps = []
	for word in words:
		end = word[-2:]
		if end == "ed":
			return word
	return "none"

def getDescriptor(astring):
	words = word_tokenize(astring)
	for word in words:
		for descriptor in DESCRIPTORS:
			if descriptor in word:
				return word
	return "none"

def getPrepDescription(astring):
	words = word_tokenize(astring)
	bis = bigrams(astring)
	for bi in bis:
		if bi[0][-2:] == "ly" and bi[1][-2:] == "ed":
			return bi[0]
	return "none"



def isNum(astring):
	num_reg = re.compile('\d*([.,\/]?\d+)')
	isMatch = num_reg.match(astring)
	if isMatch:
		return True
	return False

def list2string(alist):
	return ' '.join(alist)

def bigrams(alist):
	j = 0
	bis = []
	while j < (len(alist) - 1):
		bis.append([alist[j],alist[j+1]])
		j += 1
	return bis


MEASUREMENTS = ['teaspoon','cup','tablespoon','pint','quart','gallon','pound','once','liter','pinch'];

DESCRIPTORS = ['small','large','medium','fresh','ripe']

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