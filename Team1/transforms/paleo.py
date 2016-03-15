from collections import defaultdict
from copy import deepcopy

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

red_meat = ["beef","veal","pork","lamb","mutton","goat","hot dog","sausage","corned beef","beef jerky","bologna","salami","horse" "bacon"]
good_meat = ["turkey","chicken"]
lowfat = {}
for meat in red_meat:
	lowfat[meat] = good_meat

lowfat["ice cream"] = "sorbet"
lowfat["yogurt"] = "low fat yogurt"
lowfat["cream cheese"] = "low fat cream cheese"
lowfat["sour cream"] = "plain low-fat yogurt"
lowfat["coffee creamer"] = "low-fat milk"
lowfat["coffee cream"] = "low-fat milk"
lowfat["alfredo sauce"] = "marinara sauce"
lowfat["granola"] = "reduced-fat granola"
lowfat["croissant"] = "french roll"
lowfat["butter"] = "diet margarine"
lowfat["mayonnaise"] = "light mayonnaise"
lowfat["avocado"] = "cucumber"
lowfat["vegetable oil"] = "olive oil"
lowfat["coconut oil"] = "olive oil"
lowfat["canola oil"] = "olive oil"
lowfat["guacamole"] = "salsa"


def createHighFatMapping(theDict):
	highFat = Dictlist()
	for key, value in theDict.iteritems():
		if type(value) is not list:
			highFat[value] = key
			continue
		for unit in value:
			highFat[unit] = key

	return highFat


def toLowFat(recipe):
	recipe = deepcopy(recipe)
	ings = []
	for ing in recipe['ingredients']:
		new_ings = [ing]
		for item in lowfat:
			if item in ing['name']:
				new_ings = makeIng(lowfat[item], ing["quantity"], ing["measurement"],ing["descriptor"], ing["preparation"],ing["prep-description"])
				break
		for _ing in new_ings:
			ings.append(_ing)
	recipe['ingredients'] = ings
	return recipe	

def fromLowFat(recipe):
	recipe = deepcopy(recipe)
	ings = []
	for ing in recipe['ingredients']:
		new_ings = [ing]
		highFat = createHighFatMapping(lowfat)
		for item in highFat:
			if item in ing['name']:
				new_ings = makeIng(highFat[item], ing["quantity"], ing["measurement"],ing["descriptor"], ing["preparation"],ing["prep-description"])
				break
		for _ing in new_ings:
			ings.append(_ing)
	recipe['ingredients'] = ings
	return recipe
	

NONPAL_SUBS = ['coconut flour', 'almond milk', 'coconut cream', 'coconut aminos', 'honey', 'cauliflower rice', 'squash spaghetti', 'zucchini', 'coconut oil', 'olive oil', 'paleo bread', 'almond butter', 'nut cheese', 'flax meal']
PAL_SUBS = ['flour', 'milk', 'cream', 'soy sauce', 'sugar', 'rice', 'spaghetti', 'pasta', 'vegetable oil', 'canola oil', 'bread', 'peanut butter', 'cheese', 'butter']

def toPaleo(recipe):
	recipe = deepcopy(recipe)
	ings = []
	for ing in recipe['ingredients']:
		new_ings = [ing]
		for nonPAL in PAL_SUBS:
			if nonPAL in ing['name']:
				new_ings = subst(ing,nonPAL)
				break
		for _ing in new_ings:
			ings.append(_ing)
	recipe['ingredients'] = ings
	return recipe

def fromPaleo(recipe):
	recipe = deepcopy(recipe)
	ings = []
	for ing in recipe['ingredients']:
		new_ings = [ing]
		for meat in NONPAL_SUBS:
			if meat in ing['name']:
				new_ings = subst_nonpaleoify(ing,meat)
				break
		for new_ing in new_ings:
			ings.append(new_ing)
	recipe['ingredients'] = ings
	return recipe


def makeIng(name,quantity,measurement,descriptor,preparation,prepDescription):
	return {
		"name":name,
		"quantity":quantity,
		"measurement":measurement,
		"descriptor":descriptor,
		"preparation":preparation,
		"prep-description":prepDescription
	}

def subst_paleoify(ingredient,name):
	ings = []
	if ingredient["quantity"] == "none":
		ingredient["quantity"] = 1
	if name == "flour":
		return [makeIng("coconut flour",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'milk':
		return [makeIng("almond milk",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'cream':
		return [makeIng("coconut cream",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'soy sauce':
		return [makeIng("coconut aminos",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'sugar':
		return [makeIng("honey",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'rice':
		return [makeIng("cauliflower rice",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'spaghetti':
		return [makeIng("squash spaghetti",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'pasta':
		return [makeIng("zucchini",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'vegetable oil':
		return [makeIng("coconut oil",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'canola oil':
		return [makeIng("olive oil",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'bread':
		return [makeIng("paleo bread",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == "butter":
		return [makeIng("ghee",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == "peanut butter":
		return [makeIng("almond butter",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],"ground",ingredient['prep-description'])]
	elif name == 'cheese':
		return [makeIng("nut cheese",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'bread crumbs':
		return [makeIng("flax meal",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]


def subst(ingredient,name):
	ings = []
	if ingredient["quantity"] == "none":
		ingredient["quantity"] = 1
	if name == "flour":
		return [makeIng("coconut flour",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'milk':
		return [makeIng("almond milk",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'cream':
		return [makeIng("coconut cream",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'soy sauce':
		return [makeIng("coconut aminos",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'sugar':
		return [makeIng("honey",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'rice':
		return [makeIng("cauliflower rice",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'spaghetti':
		return [makeIng("squash spaghetti",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'pasta':
		return [makeIng("zucchini",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'vegetable oil':
		return [makeIng("coconut oil",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'canola oil':
		return [makeIng("olive oil",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'bread':
		return [makeIng("almond milk",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == "paleo bread":
		return [makeIng("ghee",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == "peanut butter":
		return [makeIng("almond butter",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],"ground",ingredient['prep-description'])]
	elif name == 'cheese':
		return [makeIng("nut cheese",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'nut cheese':
		return [makeIng("almond milk",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == 'bread crumbs':
		return [makeIng("flax meal",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]





