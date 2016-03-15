# coding=utf-8

import urllib2
from bs4 import BeautifulSoup
import nltk
import requests


def get(RECIPE_HTML):
	# primary_methods = ['bake', 'steam', 'grill', 'roast', 'boil', 'stew', 'pan-fry', 'fry','broil', 'braise', 'stew']
	# secondary_methods = ['sauté', 'saute', 'poach', 'simmer', 'barbeque', 'steam', 'blanch']


	cooking_methodsML = ['add', 'adding', 'arrange', 'arranged', 'arranging', 'bake', 'baking', 'baked', 'baste', 'basted', 'basting', 'beat', 'beating', 'blend', 'blended', 'blending', 'brown', 'browned', 'browning', 'broil', 'broiling', 'build', 'building', 'bury', 'carve', 'caring', 'carved', 'check', 'chop', 'chopped', 'chopping', 'close', 'coat', 'coated', 'coating', 'cool', 'cooling', 'combine', 'combined', 'combining', 'correct', 'correcting', 'cover', 'covering', 'crumple', 'crumpling', 'cut', 'cutting', 'decorate', 'decorating', 'discard', 'discarding', 'divide', 'dividing', 'drape', 'drop', 'dry', 'film', 'film', 'fold', 'folding', 'follow', 'form', 'force', 'glaze', 'glazed', 'glazing', 'grease', 'greasing', 'insert', 'lay', 'leave', 'lift', 'make', 'melt', 'melted', 'mince', 'minced', 'mix', 'mixed', 'moisten', 'mound', 'open', 'pack', 'paint', 'pierce', 'pierced', 'place', 'placed', 'pour', 'prepare', 'press', 'prick', 'pull', 'puree', 'push', 'preheat', 'preheated', 'quarter', 'quareted', 'raise', 'raised', 'reduce', 'reduced', 'refresh', 'reheat', 'reheated', 'replace', 'replaced', 'return', 'ring', 'roast', 'roasted', 'roll', 'rolled', 'salt', 'salted', 'saute', 'saut\xc3\xa9', 'saut\xc3\xa9d', 'sauted', 'scatter', 'scattered', 'scoop', 'scooped', 'scrape', 'scraped', 'scrub', 'season', 'seasoned', 'separate', 'separated', 'set', 'settle', 'shave', 'simmer', 'simmered', 'skim', 'skimmed', 'slice', 'sliced', 'slide', 'slip', 'slit', 'smear', 'smeared', 'soak', 'spoon', 'spread', 'sprinkle', 'sprinkled', 'squeeze', 'squeezed', 'stir', 'stirred', 'strain', 'strained', 'strew', 'stuff', 'stuffed', 'surround', 'taste', 'thin', 'thinned', 'tie', 'tied', 'tilt', 'tilted', 'tip', 'top', 'toss', 'tossed', 'trim', 'trimmed', 'turn', 'turning', 'twist', 'warm', 'warmed', 'wilt', 'wind','wrap','wrapped']
	new_list = [w.lower() for w in cooking_methodsML]

	directions = []
	
	for i in RECIPE_HTML.find_all("span", {"class":"recipe-directions__list--item"}):
		words = i.get_text()
		direction_step_words = nltk.tokenize.word_tokenize(words)
		tempDirections = [w.lower() for w in direction_step_words]
		directions += tempDirections
		unicode_directions = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in directions]

	recipe_cookingmethods = [];
	#print set(directions)
	recipe_cookingmethods = list(set(unicode_directions).intersection(new_list))

	for word in directions:
		if word in cooking_methodsML:
				recipe_cookingmethods.append(word)
	
	new_recipe_cookingmethods = list(recipe_cookingmethods)
	return new_recipe_cookingmethods



def getPrimary(RECIPE_HTML):
	primary_methods = ['bake','steam', 'grill', 'roast', 'boil', 'stew', 'pan-fry', 'fry','broil', 'braise', 'stew']
	secondary_methods = ['saute', 'poach', 'simmer', 'barbeque', 'steam', 'blanch']

	all_methods = get(RECIPE_HTML)


	for word in all_methods:
		if word in primary_methods:
			return word

	for word in all_methods:
		if word in secondary_methods:
			return word