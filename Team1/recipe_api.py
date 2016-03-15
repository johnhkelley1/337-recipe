'''Version 0.1'''

from modules import ingredients
from modules import tools
from modules import methods
from modules import steps

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

    results["primary cooking method"] = methods.getPrimary(page)
    results["cooking methods"] = methods.get(page)

    results["steps"] = steps.get(page,results)

    return results

    #print ingredients.get(RECIPE_HTML)
    #tools.get(RECIPE_HTML)
    #methods.get(RECIPE_HTML)

def tesTranformVegan():
    recipe = getRecipe("http://allrecipes.com/Recipe/Meatball-Nirvana/")
    vrecipe = vegan.toVegan(recipe)
    vrecipe = vegan.toMeat(vrecipe)
    pprint.pprint(vrecipe)

def testSteps():
    r = requests.get("http://allrecipes.com/Recipe/Meatball-Nirvana/")
    soup = BeautifulSoup(r.text, 'html.parser')
    RECIPE_HTML = soup
    page = RECIPE_HTML

    results = {}
    results["ingredients"] = ingredients.get(page)
    results["cooking tools"] = tools.get(page)
    results["primary cooking method"] = "bake"
    results["cooking methods"] = ["bake","cook","broil"]
    steps.get(page,results)

