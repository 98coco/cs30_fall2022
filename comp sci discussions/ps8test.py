import ps8sol as ps8

# question 1
def test_greetPlayer():
	joeBruin  = {"score": 1000, 
	             "location": {"x": 0, "y": -10}, 
	             "health": 50, 
	             "name": "Joe Bruin"}

	janeBruin = {"score": 20, 
	             "location": {"x": 0, "y": -10}, 
	             "health": -1, 
	             "name": "Jane Bruin"}
	assert ps8.greetPlayer(joeBruin) == "Hello, Joe Bruin!"
	assert ps8.greetPlayer(janeBruin) == "You are Dead!"

# question 2
def test_movePlayer():
	joeBruin  = {"score": 1000, 
	             "location": {"x": 0, "y": -10}, 
	             "health": 50, 
	             "name": "Joe Bruin"}

	janeBruin = {"score": 20, 
	             "location": {"x": 0, "y": -10}, 
	             "health": -1, 
	             "name": "Jane Bruin"}
	player1 = ps8.movePlayer(joeBruin, 500, 500, 1000)
	assert player1["name"] == 'Joe Bruin'
	assert player1["location"] == {'x': 500, 'y': 500}
	assert player1["health"] == 50
	assert player1["score"] == 1000

	player2 = ps8.movePlayer(janeBruin, 500, 500, 1000)
	assert player2["name"] == 'Jane Bruin'
	assert player2["location"] == {'x': 0, 'y': -10}
	assert player2["health"] == -1
	assert player2["score"] == 20

# question 3
def test_multiplyByi(): 
	assert ps8.multiplyByi([{"real": 1, "im": 2}, {"real": -1, "im": -4}]) == [{"real": -2, "im": 1}, {"real": 4, "im": -1}]
	assert ps8.multiplyByi([{"real": -1, "im": 2}, {"real": 1, "im": -4}]) == [{"real": -2, "im": -1}, {"real": 4, "im": 1}]
	assert ps8.multiplyByi([]) == []

# question 4
def test_count_7():
	assert ps8.count_7([1,17,72]) == 2
	assert ps8.count_7([77, 73, 177, 0]) == 3

# question 5
def test_series():
	assert ps8.series(4) == 2.083
	assert ps8.series(7) == 2.593

# question 6
def test_multTable():
	assert ps8.multTable(6) == [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
	assert ps8.multTable(11) == [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]

# question 7
def test_maxRationals():
	assert ps8.maxRationals([{"num": 1, "denom": 2}, {"num": 1, "denom": 4}]) == {"num": 1, "denom": 2}
	assert ps8.maxRationals([{"num": 1, "denom": 3}, {"num": 2, "denom": 9}, {"num": 3, "denom": 13}]) == {"num": 1, "denom": 3}

# question 8
def test_findGreatestRelevance():
	searchResults = [
    {"title": "The Perfect Cranberry Sauce", "keywords": ["cranberries"], "relevance": 25},
    {"title": "Roasting a Turkey: 101", "keywords": ["bird"], "relevance": 88},
    {"title": "How Not to Ruin Thanksgiving", "keywords": ["social gathering", "thanksgiving"], "relevance": 25},
    {"title": "How to Bake a Pie", "keywords": ["baking", "pie"], "relevance": 9},
    {"title": "One Hundred Things Your Uncle Shouldn't Say at Thanksgiving",
     "keywords": ["inappropriate behavior", "thanksgiving"], "relevance": 1},
    {"title": "How To Stuff a Turkey", "keywords": ["turkey", "stuffing", "baking advice"], "relevance": 88},
	]
	assert ps8.findGreatestRelevance(searchResults) == 88

# question 9
def test_findNamesOfGreatestRelevance():
	searchResults = [
    {"title": "The Perfect Cranberry Sauce", "keywords": ["cranberries"], "relevance": 25},
    {"title": "Roasting a Turkey: 101", "keywords": ["bird"], "relevance": 88},
    {"title": "How Not to Ruin Thanksgiving", "keywords": ["social gathering", "thanksgiving"], "relevance": 25},
    {"title": "How to Bake a Pie", "keywords": ["baking", "pie"], "relevance": 9},
    {"title": "One Hundred Things Your Uncle Shouldn't Say at Thanksgiving",
     "keywords": ["inappropriate behavior", "thanksgiving"], "relevance": 1},
    {"title": "How To Stuff a Turkey", "keywords": ["turkey", "stuffing", "baking advice"], "relevance": 88},
	]
	assert ps8.findNamesOfGreatestRelevance(searchResults) == ['Roasting a Turkey: 101', 'How To Stuff a Turkey']

# question 10
def test_mostRelevantWithThanksgiving():
	searchResults = [
    {"title": "The Perfect Cranberry Sauce", "keywords": ["cranberries"], "relevance": 25},
    {"title": "Roasting a Turkey: 101", "keywords": ["bird"], "relevance": 88},
    {"title": "How Not to Ruin Thanksgiving", "keywords": ["social gathering", "thanksgiving"], "relevance": 25},
    {"title": "How to Bake a Pie", "keywords": ["baking", "pie"], "relevance": 9},
    {"title": "One Hundred Things Your Uncle Shouldn't Say at Thanksgiving",
     "keywords": ["inappropriate behavior", "thanksgiving"], "relevance": 1},
    {"title": "How To Stuff a Turkey", "keywords": ["turkey", "stuffing", "baking advice"], "relevance": 88},
	]
	assert ps8.mostRelevantWithThanksgiving(searchResults) == ['How Not to Ruin Thanksgiving']

# question 11
def test_averageLengthAbovek():
	searchResults = [
    {"title": "The Perfect Cranberry Sauce", "keywords": ["cranberries"], "relevance": 25},
    {"title": "Roasting a Turkey: 101", "keywords": ["bird"], "relevance": 88},
    {"title": "How Not to Ruin Thanksgiving", "keywords": ["social gathering", "thanksgiving"], "relevance": 25},
    {"title": "How to Bake a Pie", "keywords": ["baking", "pie"], "relevance": 9},
    {"title": "One Hundred Things Your Uncle Shouldn't Say at Thanksgiving",
     "keywords": ["inappropriate behavior", "thanksgiving"], "relevance": 1},
    {"title": "How To Stuff a Turkey", "keywords": ["turkey", "stuffing", "baking advice"], "relevance": 88},
	]
	assert ps8.averageLengthAbovek(searchResults, 25) == 24.5

# question 12
def test_isPrime():
	assert ps8.isPrime(0) == False
	assert ps8.isPrime(2) == True
	assert ps8.isPrime(7) == True
	assert ps8.isPrime(91) == False

# question 13
def test_getPrimes():
	assert ps8.getPrimes(10) == [2, 3, 5, 7]
	assert ps8.getPrimes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

# question 14
def test_draw():
	assert ps8.draw(4) == '#\n##\n###\n####\n'
	assert ps8.draw(5) == '#\n##\n###\n####\n#####\n'

# question 15
def test_maxOfInnerList():
	assert ps8.maxOfInnerList([[1,2,3], [7,2,3], [8,10,9]]) == [3, 7, 10]
	assert ps8.maxOfInnerList([[-1,-2,-3], [-2,-7], [-8,-10]]) == [-1, -2, -8]

