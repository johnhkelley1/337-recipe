import re
from copy import deepcopy
from random import choice

SAUCES = ['sauce', 'gravy', 'mayonnaise', 'ketchup']

OILS   = ['margerine', 'oil', 'butter']

VEGIS  = ['lemon', 'mushroom', 'beet', 'bell pepper', 'lettuce', 'cabbage',
          'corn', 'peas', 'kale', 'spinach', 'avocado', 'tomato', 'melon',
          'eggplant', 'zucchini', 'squash', 'artichoke', 'broccoli',
          'cauliflower', 'celery', 'chives', 'onion', 'leek', 'carrot',
          'ginger']

SPICES = ['oregano', 'salt', 'pepper', 'thyme', 'garlic powder', 'cumin',
          'spice']

ING_SUBS = {
    'american': {
        'sauces': ['ketchup', 'mayonnaise'],
        'oils': ['butter', 'margerine'],
        'vegis': ['french fries', 'tater tots', 'caesar salad'],
        'spices': ['salt', 'pepper']
    },
    'chinese': {
        'sauces': ['soy sauce', 'sweet and sour sauce', 'kung pao sauce',
                   'general tso sauce'],
        'oils': ['soybean oil'],
        'vegis': ['bok choy', 'chinese eggplant', 'bitter melon'],
        'spices': ['msg', 'red pepper flakes', 'sichuan pepper']
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

    spice = False
    spice_q = None
    spice_m = None
    spice_d = None
    spice_p = None
    spice_pd = None

    new_sauce = choice(ING_SUBS[cuisine]['sauces'])
    new_oil = choice(ING_SUBS[cuisine]['oils'])
    new_vegi = choice(ING_SUBS[cuisine]['vegis'])
    new_spice = choice(ING_SUBS[cuisine]['spices'])

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
                for step in recipe['steps']:
                    temp_ings = step['ingredients'][:]
                    if temp_ings == 'none':
                        continue
                    step['ingredients'] = [d for d in temp_ings if d != ing['name']]
                    step['ingredients'].append(new_sauce)
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
                for step in recipe['steps']:
                    temp_ings = step['ingredients'][:]
                    if temp_ings == 'none':
                        continue
                    step['ingredients'] = [d for d in temp_ings if d != ing['name']]
                    step['ingredients'].append(new_oil)
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
                for step in recipe['steps']:
                    temp_ings = step['ingredients'][:]
                    if temp_ings == 'none':
                        continue
                    step['ingredients'] = [d for d in temp_ings if d != ing['name']]
                    step['ingredients'].append(new_vegi)
                continue

        # Check spice
        for s in SPICES:
            if re.search(s, ing['name'], re.IGNORECASE):
                spice = True
                spice_q = ing['quantity']
                spice_m = ing['measurement']
                spice_d = ing['descriptor']
                spice_p = ing['preparation']
                spice_pd = ing['prep-description']

                temp_ings = recipe['ingredients'][:]
                recipe['ingredients'] = [d for d in temp_ings if d['name'] != ing['name']]
                for step in recipe['steps']:
                    temp_ings = step['ingredients'][:]
                    if temp_ings == 'none':
                        continue
                    step['ingredients'] = [d for d in temp_ings if d != ing['name']]
                    step['ingredients'].append(new_spice)
                continue

    if sauce:
        recipe['ingredients'].append({
    		"name": new_sauce,
    		"quantity": sauce_q,
    		"measurement": sauce_m,
    		"descriptor": sauce_d,
    		"preparation": sauce_p,
    		"prep-description": sauce_pd
    	})

    if oil:
        recipe['ingredients'].append({
    		"name": new_oil,
    		"quantity": oil_q,
    		"measurement": oil_m,
    		"descriptor": oil_d,
    		"preparation": oil_p,
    		"prep-description": oil_pd
    	})

    if vegi:
        recipe['ingredients'].append({
    		"name": new_vegi,
    		"quantity": vegi_q,
    		"measurement": vegi_m,
    		"descriptor": vegi_d,
    		"preparation": vegi_p,
    		"prep-description": vegi_pd
    	})

    if spice:
        recipe['ingredients'].append({
    		"name": new_spice,
    		"quantity": spice_q,
    		"measurement": spice_m,
    		"descriptor": spice_d,
    		"preparation": spice_p,
    		"prep-description": spice_pd
    	})

    return recipe
