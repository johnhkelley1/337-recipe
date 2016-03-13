import requests
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize
import re

def get(RECIPE_HTML):
	unigram_tools = ["whisk","grater","shears","colander","spoon","knife","fork",
	"mandoline","slicer","strainer","mortar","pestle","dropper",
	"baster","thermometer","pan","saucepan",
	"crisper","skillet","griddle","braiser","roaster",
	"wok","kettle","pot","timer","corkscrew","decanter",
	"spatula","ladle","tongs","skimmer","refrigerator","oven","microwave","toaster"]

	bigram_tools = ["baking dish","measuring cup","cutting board", "kitchen shears", "eye dropper","can opener","mixing bowl","steak knife",
	"salt mill","pepper mill","baking sheet","aluminum foil","pizza stone","pizza wheel","cookie sheet","loaf pan","brioche pan","frying pan","fry pan","baking pan",
	"saute pan","dutch oven","tea kettle","oil dispenser","wine opener","serving dish","wood spoon","wooden spoon", "non-stick foil","oven broiler"]

	trigram_tools = ["cast iron skillet","non-stick aluminum foil","mircrowave safe bowl","microwave safe dish","microwave safe plate","stainless steel pot","stainless steel pan","stainless steel "]

	stopwords = [".",":",";","-","'",","]
	directions = []
	final_directions_words = []
	bigrams_final = []
	trigrams_final = []
	tools_final = []

	for i in RECIPE_HTML.find_all("span", {"class":"recipe-directions__list--item"}):
		words = i.get_text()
		direction_step_words = nltk.tokenize.word_tokenize(words)
		tempDirections = [w.lower() for w in direction_step_words]
		directions += tempDirections
		
		
	for i in directions:
		if i not in stopwords:
			final_directions_words.append(i)



	#print final_directions_words
	for i in final_directions_words:
		if i == "baste":
			del i
			final_directions_words.append("baster")
		if i == "stir":
			del i
			final_directions_words.append("spoon")


	bigrams_in_directions = list(nltk.bigrams(final_directions_words))
	trigrams_in_directions = list(nltk.trigrams(final_directions_words))

	for i in bigrams_in_directions:
		tempBigram = i[0] + " " + i[1]
		bigrams_final.append(tempBigram)

	#print "========================"

	for i in trigrams_in_directions:
		tempTrigram = i[0] + " " + i[1] + " " + i[2]
		trigrams_final.append(tempTrigram)

	#print trigrams_final


	#check matches b/w trigrams_final and trigram_tools
	tools_final += set(trigrams_final).intersection(trigram_tools)

	#check matches b/w bigrams_final and bigram_tools
	tools_final += set(bigrams_final).intersection(bigram_tools)

	#check matches between final_directions_words and unigrams_tools
	tools_final += set(final_directions_words).intersection(unigram_tools)

	return tools_final


