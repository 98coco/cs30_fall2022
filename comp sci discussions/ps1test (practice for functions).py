import ps1
#import ps1sol as ps1

def test_cubic():
        assert ps1.cubic(2) == 8
        assert ps1.cubic(3) == 27
	
def test_differenceOfCubics():
	assert ps1.differenceOfCubics(3,2) == 19
	assert ps1.differenceOfCubics(5,3) == 98

def test_permutation3():
	assert ps1.permutation3(10) == 720

def test_combination3():
	assert ps1.combination3(10) == 120

def test_checkStartEndString():
	assert ps1.checkStartEndString("apple") == True
	assert ps1.checkStartEndString("banana") == False

def test_checkStartEndList():
	assert ps1.checkStartEndList(["apple pie", "banana", "apple","juice","apple juice","orange juice","coconut","coconut juice"]) == True
	assert ps1.checkStartEndList(["coconut","coconut juice", "apple pie", "banana", "apple","juice","apple juice","orange juice"]) == False

def test_calcList8():
	assert ps1.calcList8([1, 2, 3, 4,   5,  6, 7, 8]) == [1, 8, 0, 100, 26, 6, 7, 8]

