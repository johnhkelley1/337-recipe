import re
from copy import deepcopy
from random import choice

SAUCES = ['sauce', 'gravy', 'mayonnaise']

OILS   = ['margerine', 'oil', 'olive oil', 'vegitable oil', 'butter']

VEGIS  = ['lemon', 'mushroom', 'beet', 'bell pepper', 'lettuce', 'cabbage',
          'corn', 'peas', 'kale', 'spinach', 'avocado', 'tomato', 'melon',
          'eggplant', 'zucchini', 'squash', 'artichoke', 'broccoli',
          'cauliflower', 'celery', 'chives', 'onion', 'leek', 'carrot',
          'ginger']

ING_SUBS = {
    'american': {
        'sauces': ['ketchup', 'mayonnaise'],
        'oils': ['butter', 'margerine'],
        'vegis': ['french fries', 'tater tots', 'caesar salad']
    },
    'chinese': {
        'sauces': ['soy sauce', 'sweet and sour sauce', 'kung pao sauce'],
        'oils': ['soybean oil'],
        'vegis': ['bok choy', 'chinese eggplant', 'bitter melon']
    }
}


def toCuisine(recipe, cuisine):
    recipe = deepcopy(recipe)

    sauce = False
    sauce_q = None
    sauce_m = None
    sauce_d = None
    sauce_p = None
    sauce_pd = None

    oil = False
    oil_q = None
    oil_m = None
    oil_d = None
    oil_p = None
    oil_pd = None

    vegi = False
    vegi_q = None
    vegi_m = None
    vegi_d = None
    vegi_p = None
    vegi_pd = None

    for ing in recipe['ingredients']:
        # Check sauce
        for s in SAUCES:
            if re.search(s, ing['name'], re.IGNORECASE):
                sauce = True
                sauce_q = ing['quantity']
                sauce_m = ing['measurement']
                sauce_d = ing['descriptor']
                sauce_p = ing['preparation']
                sauce_pd = ing['prep-description']

                temp_ings = recipe['ingredients'][:]
                recipe['ingredients'] = [d for d in temp_ings if d['name'] != ing['name']]
                continue

        # Check oil
        for o in OILS:
            if re.search(o, ing['name'], re.IGNORECASE):
                oil = True
                oil_q = ing['quantity']
                oil_m = ing['measurement']
                oil_d = ing['descriptor']
                oil_p = ing['preparation']
                oil_pd = ing['prep-description']

                temp_ings = recipe['ingredients'][:]
                recipe['ingredients'] = [d for d in temp_ings if d['name'] != ing['name']]
                continue

        # Check vegi
        for v in VEGIS:
            if re.search(v, ing['name'], re.IGNORECASE):
                vegi = True
                vegi_q = ing['quantity']
                vegi_m = ing['measurement']
                vegi_d = ing['descriptor']
                vegi_p = ing['preparation']
                vegi_pd = ing['prep-description']

                temp_ings = recipe['ingredients'][:]
                recipe['ingredients'] = [d for d in temp_ings if d['name'] != ing['name']]
                continue

    if sauce:
        recipe['ingredients'].append({
    		"name": choice(ING_SUBS[cuisine]['sauces']),
    		"quantity": sauce_q,
    		"measurement": sauce_m,
    		"descriptor": sauce_d,
    		"preparation": sauce_p,
    		"prep-description": sauce_pd
    	})

    if oil:
        recipe['ingredients'].append({
    		"name": choice(ING_SUBS[cuisine]['oils']),
    		"quantity": oil_q,
    		"measurement": oil_m,
    		"descriptor": oil_d,
    		"preparation": oil_p,
    		"prep-description": oil_pd
    	})

    if vegi:
        recipe['ingredients'].append({
    		"name": choice(ING_SUBS[cuisine]['vegis']),
    		"quantity": vegi_q,
    		"measurement": vegi_m,
    		"descriptor": vegi_d,
    		"preparation": vegi_p,
    		"prep-description": vegi_pd
    	})

    return recipe
