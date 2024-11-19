import ps5 as ps5

# question 1
def test_minutesToSeconds():
	assert ps5.minutesToSeconds([1,2,3]) == [60,120,180]
	assert ps5.minutesToSeconds([5,6,9]) == [300,360,540]
	assert ps5.minutesToSeconds([]) == []
	assert ps5.minutesToSeconds([0]) == [0]

# question 2
def test_Fahren2Cels():
	assert ps5.Fahren2Cels([72,32,0]) == [22, 0, -18]
	assert ps5.Fahren2Cels([]) == []
	
# question 3
def test_punctuation():
	assert ps5.punctuation(['hello?', 'world']) == ['world!']

# question 4
def test_average():
	assert ps5.average([1,2,3,4]) == 2.5

# question 5
def test_pennypincher():
	assert ps5.pennypincher([100, 150, 200, 210, 250]) == 594

# question 6
def test_crosswordFind():
	assert ps5.crosswordFind('k', 1, 7, ["funky", "fabulous", "kite", "icky", "ukelele"]) == ["ukelele"]
