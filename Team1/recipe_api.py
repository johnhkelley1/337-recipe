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

def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]

def printRecipe(recipe):
    pprint.pprint(recipe)

choice = ""
url    = None
recipe = None
while True:

    # Get URL
    if url is None:
        url = raw_input("Enter the URL of the recipe: ")
        recipe = getRecipe(url)

    print "\nChoose from the following options:"
    print "  (0) View Current Recipe"
    print "  (1) Transform Recipe"
    print "  (2) New Recipe"
    print "  (q) Quit"
    print "\n  Your choice:",
    choice = raw_input()

    # Break if choice == q
    if choice.lower() == 'q':
        break
    else:
        choice = int(choice)

    # Make sure choice is valid
    if choice < 0 or choice > 2:
        print "Invalide choice!"
        continue

    # Run function based off of choice
    if choice == 0:
        printRecipe(recipe)
    elif choice == 1:
        print "\n Choose your transformation:"
        print "  (0) American Cuisine"
        print "  (1) Chinese Cuisine"
        print "\n  Your choice:",
        choice = int(raw_input())

        # Make sure choice is valid
        if choice < 0 or choice > 1:
            print "Invalide choice!"
            continue

        new_recipe = None
        if choice == 0:
            new_recipe = cuisine.toCuisine(recipe, 'american')
        elif choice == 1:
            new_recipe = cuisine.toCuisine(recipe, 'chinese')

        pprint.pprint(new_recipe)
        ings     = [ing['name'] for ing in recipe['ingredients']]
        ings_new = [ing['name'] for ing in new_recipe['ingredients']]
        removed   = diff(ings, ings_new)
        added = diff(ings_new, ings)

        print "\nIngredients Added:"
        print added
        print "\nIngredients Removed:"
        print removed

    elif choice == 2:
        url = None
        continue



print "\nGoodbye!"
