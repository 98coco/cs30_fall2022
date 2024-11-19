import ps2
#import ps2sol as ps2

# question 1
def test_larger_between_two():
	# add two more test cases here
	assert ps2.larger_between_two(4,5) == 5
	assert ps2.larger_between_two(7,8) == 8
	assert ps2.larger_between_two(9,3) == 9

# qeustion 2
def test_largest_among_three():
	# add two more test cases here
	assert ps2.largest_among_three(4,5,6) == 6
	assert ps2.largest_among_three(7,8,6) == 8
	assert ps2.largest_among_three(10,7,5) == 10
	assert ps2.largest_among_three(4,5,2) == 5
	

# qeustion 3
def test_largest_in_list():
	# add two more test cases here
	assert ps2.largest_in_list([]) == 0
	assert ps2.largest_in_list([1, 2, 3]) == 3
	assert ps2.largest_in_list([4, 9, 12]) == 12
	assert ps2.largest_in_list([10, 11, 15]) == 15

# question 4 [optional]
def test_whatToCook():
	# add at least two more test cases
	assert ps2.whatToCook(1, 0, 0, 3) == "Kabob"

# question 5
def test_doubleEachElement():
	assert ps2.doubleEachElement([1, 2, 3, 4]) == [2, 4, 6, 8]
	assert ps2.doubleEachElement([2, 5, 6, 7]) == [4, 10, 12, 14]
	assert ps2.doubleEachElement([3, 4, 5, 8]) == [6, 8, 10, 16]

# question 6
def test_sumEven():
	assert ps2.sumEven([1, 2, 4]) == 6
	assert ps2.sumEven([3, 8, 10]) == 18
	assert ps2.sumEven([4, 7, 2]) == 6
	assert ps2.sumEven([5, 8, 12]) == 20
	

# question 7
def test_filterNegativeNumbers():
	assert ps2.filterNegativeNumbers([1, -2, 3, -4]) == [1, 3]
	assert ps2.filterNegativeNumbers([1, -1, 5, 0, 3]) == [1, 5, 0, 3]
	assert ps2.filterNegativeNumbers([-5, -3, 5, 0, 3]) == [5, 0, 3]
	assert ps2.filterNegativeNumbers([-1, -5, -5,-3]) == []
