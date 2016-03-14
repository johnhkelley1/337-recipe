from bs4 import BeautifulSoup
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
import re

word_tokenize = nltk.tokenize.TreebankWordTokenizer().tokenize

def get(recipe,recipe_obj):
	steps = []
	stepsParsed = []
	for i in recipe.findAll("span",class_="recipe-directions__list--item"):
		steps.append(i.text)
	
	alen = len(steps)
	for i in range(alen - 1):
		words = word_tokenize(steps[i])
		words = [word.lower() for word in words]

		steps[i] = steps[i].lower()


		for item in recipe_obj:
			if item == "none":
				item = []


		stepsParsed.append({"step_num":i+1})

		stepsParsed[i]['ingredients'] = []
		stepsParsed[i]['tools'] = []
		stepsParsed[i]['methods'] = []

		for ingredient in recipe_obj["ingredients"]:
			if ingredient["name"] in steps[i]:
				stepsParsed[i]['ingredients'].append(ingredient["name"])

		if len(stepsParsed[i]['ingredients']) == 0:
			stepsParsed[i]['ingredients'] = "none"

		for tool in recipe_obj["cooking tools"]:
			if tool in steps[i]:
				stepsParsed[i]['tools'].append(tool)

		if len(stepsParsed[i]['tools']) == 0:
			stepsParsed[i]['tools'] = "none"

		for method in recipe_obj["cooking methods"]:
			if method in steps[i]:
				stepsParsed[i]['methods'].append(method)

		if len(stepsParsed[i]['methods']) == 0:
			stepsParsed[i]['methods'] = "none"

		time = "until done"
		for j in range(len(words)):
			for tword in TIME_WORDS:
				if tword in words[j] and j > 0:
					time = words[j-1] + " " + words[j]

		stepsParsed[i]['time'] = time


	return stepsParsed

TIME_WORDS = ['minute','second','hour']
