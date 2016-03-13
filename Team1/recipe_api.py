'''Version 0.1'''

from modules import ingredients
from modules import tools
from modules import methods

from transforms import vegan

import requests
from bs4 import BeautifulSoup
import pprint

def autograder(url):
    '''Accepts the URL for a recipe, and returns a dictionary of the
    parsed results in the correct format. See project sheet for
    details on correct format.'''
    # your code here

    return getRecipe(url)

def getRecipe(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    RECIPE_HTML = soup
    page = RECIPE_HTML

    results = {}
    results["ingredients"] = ingredients.get(page)
    results["cooking tools"] = tools.get(page)
    results["primary cooking method"] = "none"
    results["cooking methods"] = []

    return results

	#print ingredients.get(RECIPE_HTML)
	#tools.get(RECIPE_HTML)
	#methods.get(RECIPE_HTML)

def tranformVegan():
    recipe = getRecipe("http://allrecipes.com/Recipe/Meatball-Nirvana/")
    vrecipe = vegan.toVegan(recipe)
    pprint.pprint(vrecipe)

tranformVegan()
