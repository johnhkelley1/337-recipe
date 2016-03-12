'''Version 0.1'''

from modules import ingredients
from modules import tools
from modules import methods

import requests
from bs4 import BeautifulSoup

def autograder(url):
    '''Accepts the URL for a recipe, and returns a dictionary of the
    parsed results in the correct format. See project sheet for
    details on correct format.'''
    # your code here

    return results

def getRecipe(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	RECIPE_HTML = soup

	#ingredients.get(RECIPE_HTML)
	#tools.get(RECIPE_HTML)
	#methods.get(RECIPE_HTML)


getRecipe("http://allrecipes.com/Recipe/Easy-Garlic-Broiled-Chicken/")
