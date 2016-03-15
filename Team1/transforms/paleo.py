#paleo
#health
def toLowFat(recipe):
	ings = []
	for ing in recipe['ingredients']:
		new_ings = [ing]
		for meat in (VEGI_SUBS + VEGAN_SUBS):
			if meat in ing['name']:
				new_ings = subst(ing,meat)
				break
		for new_ing in new_ings:
			ings.append(new_ing)
	recipe['ingredients'] = ings
	return recipe	

def fromLowFat(recipe):

def toLowCarb(recipe):

def fromLowCarb(recipe):


paleoNoGo = ["peanuts","legumes","milk"]


def makeIng(name,quantity,measurement,descriptor,preparation,prepDescription):
	return {
		"name":name,
		"quantity":quantity,
		"measurement":measurement,
		"descriptor":descriptor,
		"preparation":preparation,
		"prep-description":prepDescription
	}



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
	
def toPaleo:
	ings = []
	for ing in recipe['ingredients']:
		new_ings = [ing]
		for nonPAL in (PAL_SUBS):
			if nonPAL in ing['name']:
				new_ings = subst(ing,nonPAL)
				break
		for new_ing in new_ings:
			ings.append(new_ing)
	recipe['ingredients'] = ings
	return recipe

PAL_SUBS = ['flour', 'milk', 'cream', 'soy sauce', 'sugar', 'rice', 'spaghetti', 'pasta', 'vegetable oil', 'canola oil', 'bread', 'peanut butter', 'cheese', 'butter']
