import ps3

# question 5
def test_taxes():
	assert ps3.taxes(30000) == 3600
	assert ps3.taxes(40000) == 5125

# question 6
def test_miniCalculator():
	assert ps3.miniCalculator(3,1,'+') == 4


# question 7
def test_q():
	# add two more test cases here
	assert ps3.q([1,12,153,84,64,9]) == True

# qeustion 8
def test_minimum():
	# add two more test cases here
	assert ps3.minimum([4,5,6]) == 4

# qeustion 9
def test_tails():
	# add two more test cases here
	assert ps3.tails([]) == [[]]
	assert ps3.tails([1, 2, 3]) == [[1,2,3], [2,3], [3], []]

# question 10
def test_flatten():
	# add at least two more test cases
	assert ps3.flatten([[1,2], [3], [], [4,5,6]]) == [1, 2, 3, 4, 5, 6]

# question 11
def test_rmDups():
	assert ps3.rmDups([1,2,2,3,3,3,4,2,2,3]) == [1, 2, 3, 4, 2, 3]

# question 12
def test_isPalindrome():
	assert ps3.isPalindrome([1, 2, 2, 1]) == True

# question 13
def test_multiplyAllByFirst():
	assert ps3.multiplyAllByFirst([]) == []
	assert ps3.multiplyAllByFirst([4, 0, 2, 5]) == [16, 0, 8, 20]