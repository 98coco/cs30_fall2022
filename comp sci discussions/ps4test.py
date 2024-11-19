import ps4 as ps4

# question 1
def test_removeOne():
	assert ps4.removeOne([1, 2, 3], 1) == [2, 3]
	assert ps4.removeOne([8, -1, 0], -1) == [8, 0]
	assert ps4.removeOne([0], 0) == []
	assert ps4.removeOne([2, 3, 2, 3], 2) == [3, 2, 3]
	assert ps4.removeOne([2, 3], 10) == [2, 3]
	assert ps4.removeOne([1,2,3], 2) == [1,3]
	assert ps4.removeOne([1,2,3,2], 2) == [1,3,2]
	assert ps4.removeOne([1,2,3], 10) == [1,2,3]

# question 2
def test_selectionSort():
	assert ps4.selectionSort([1, 3, 5, -1, 0]) == [-1, 0, 1, 3, 5]
	assert ps4.selectionSort([1, 2, 3, 1, 3, 1]) == [1, 1, 1, 2, 3, 3] 

# question 3
def test_getDigits():
	assert ps4.getDigits(123) == [1, 2, 3]
	assert ps4.getDigits(12083) == [1, 2, 0, 8, 3]
	assert ps4.getDigits(1) == [1]


# question 4
def test_getNumber():
	assert ps4.getNumber([1,2,3]) == 123
	assert ps4.getNumber([1,2,0,8,3]) == 12083
	assert ps4.getNumber([0,1]) == 1


# question 5
def test_minPossibleNumber():
	assert ps4.minPossibleNumber(2845) == 2458
	assert ps4.minPossibleNumber(31084) == 1348 


# question 6
def test_flatten():
	assert ps4.flatten([1, [1, [2, 3]]]) == [1, 1, 2, 3]
	assert ps4.flatten([[1, 2], [2, 4]]) == [1, 2, 2, 4]
	assert ps4.flatten([1,2,3,[4,5,6,[7,8,[9]]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert ps4.flatten([]) == []
