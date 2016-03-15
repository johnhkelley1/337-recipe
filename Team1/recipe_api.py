'''Version 0.1'''

from modules import ingredients
from modules import tools
from modules import methods
from modules import steps

from transforms import vegan
from transforms import cuisine

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

def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]

def testCuisine():
    recipe = getRecipe("http://allrecipes.com/Recipe/Meatball-Nirvana/")
    arecipe = cuisine.toCuisine(recipe, 'american')
    crecipe = cuisine.toCuisine(recipe, 'chinese')

    ings1 = [ing['name'] for ing in recipe['ingredients']]
    ings2 = [ing['name'] for ing in arecipe['ingredients']]
    ings3 = [ing['name'] for ing in crecipe['ingredients']]

    pprint.pprint(diff(ings1, ings2))
    pprint.pprint(diff(ings2, ings1))
    pprint.pprint(diff(ings3, ings1))

testCuisine()
