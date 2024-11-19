import ps6 as ps6


# question 1
def test_doubleLargeStrings():
	assert ps6.doubleLargeStrings(['hello','world','!']) == [['hello','hello'],['world','world']]
	assert ps6.doubleLargeStrings(['hello','','!']) == [['hello','hello']]
	assert ps6.doubleLargeStrings(['hello','world']) == [['hello','hello'],['world','world']]
	assert ps6.doubleLargeStrings(['']) == []

# question 2
def test_noZeroLists():
	assert ps6.noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]]) == [[1,2,3], [], [1,1,1]]

def test_noZeroLists_2():
	assert ps6.noZeroLists_2([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]]) == [[1,2,3], [], [1,1,1]]

# question 3
def test_count():
	assert ps6.count(2, [1, 2, 2, 3, 2]) == 3

# question 4
def test_innerMultiply():
	assert ps6.innerMultiply([[1,2,3], [4,5]], 10) == [[10,20,30], [40,50]]

# question 5
def test_g():
	assert ps6.g([1,3,6,5]) == 13

# question 6
def test_pairify():
	assert ps6.pairify([1,5,6,8,9,10]) == [[1,5], [6,8], [9,10]]

# question 7
def test_zip():
	assert ps6.zip([1,2,3], [4,5,6]) == [[1,4], [2,5], [3,6]]
	assert ps6.zip([1], [4]) == [[1, 4]]
	assert ps6.zip([], []) == []

# question 8
def test_unzip():
	assert ps6.unzip([[1,4], [2,5], [3,6]]) == [[1,2,3], [4,5,6]]

# question 9
def test_zip():
	assert ps6.allsublists([1, 2, 3]) == [[], [1], [2], [3], [1,2], [1,3], [2, 3], [1, 2, 3]]
	assert ps6.allsublists([1,1]) == [[], [1], [1], [1,1]]
