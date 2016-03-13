def toVegan(recipe):
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

def toVegitarian(recipe):
	ings = []
	for ing in recipe['ingredients']:
		new_ings = [ing]
		for meat in VEGI_SUBS:
			if meat in ing['name']:
				new_ings = subst(ing,meat)
				break
		for new_ing in new_ings:
			ings.append(new_ing)
	recipe['ingredients'] = ings
	return recipe



def subst(ingredient,name):
	ings = []
	if ingredient["quantity"] == "none":
		ingredient["quantity"] = 1
	if name == "beef":
		#ing = makeIng("canned beans",ingredient["quantity"],ingredient["measurement"],ingredient["descriptor"],ingredient["preparation"],ingredient["prep-description"])
		ing = makeIng("cooked beans",ingredient["quantity"]/2,ingredient["measurement"],"cooked","drained and rinsed","none")
		ings.append(ing)
		ing = makeIng("clove garlic",1,"units",'minced','minced',"none")
		ings.append(ing)
		ing = makeIng("onion",round(ingredient["quantity"]/3,3),ingredient["measurement"],'none','chopped',"none")
		ings.append(ing)
		ing = makeIng("diced vegies",ingredient["quantity"]/2,ingredient["measurement"],"none","diced","none")
		ings.append(ing)
		return ings
	elif name == 'milk':
		return [makeIng("almond milk",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == "butter":
		return [makeIng("margarine",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]
	elif name == "cheese":
		return [makeIng("ground almonds",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],"ground",ingredient['prep-description'])]
	return [makeIng("tofu",ingredient['quantity'],ingredient['measurement'],ingredient['descriptor'],ingredient['preparation'],ingredient['prep-description'])]

def makeIng(name,quantity,measurement,descriptor,preparation,prepDescription):
	return {
		"name":name,
		"quantity":quantity,
		"measurement":measurement,
		"descriptor":descriptor,
		"preparation":preparation,
		"prep-description":prepDescription
	}

VEGI_SUBS = ['chicken','beef','bacon','pork','ham','crab','duck','goose','lamb','meat','poultry','veal','boar','steak','venison','turkey','quail','pheasant','rabbit','fish','cod','salmon','oyster']
VEGAN_SUBS = ['milk','butter','egg','cheese']
