# 1. Implement the test for the function 'cubic' that takes an input and returns the cubic
# of the input.
#    Example: input: 2
#             return value: 8
def cubic(input):
	return pow(input, 3)
	

# 2. Implement a function differenceOfCubics that takes two input numbers and
# returns the difference of their cubics. Make use of cubic function that you
# have already written.
# Example: input : n1 = 3, n2 = 2
#          return value : 19
def differenceOfCubics(n1, n2):
        n1 = pow(n1,3)
        n2 = pow(n2,3)
        return n1 - n2


# 3. Implement function permutation3 that takes as input number of t-shirts n,
# and returns the number of different unique ways to dress for Monday, Tuesday, and Wednesday.
# We assume each shirt will get dirty by the end of day and thus can only be worn once. 
# Assume n > 3.
#   Example In : n = 10,
#           Out : 720
#   Hint : Please lookup the math concept of permutation 
def permutation3(n):
	return n*(n-1)*(n-2)

# 4. Implement function combination3 that takes as input total group size n
# and returns number of possible teams of 3 students from the group. 
# please try to use function permutation3(n). Assume n > 3.
#   Example In : n = 10, 
#           Out : 120
#   Hint : Please lookup the math concept of combination
def combination3(n):
	return n*(n-1)*(n-2)/(3*2)
	
########## string ###########

# 5. Write a function checkStartEndString(s), which takes in a string s and returns True
# if and only if the first character in s is "a" and the last character in
# s is "e". you can assume the input string has at least 2 charactors
# Example: In: s = 'apple pie'
#          Out: True
#          In: s = 'apple music'
#          Out: False
def checkStartEndString(s):
	# assume s is not empty
	Combination1 = (s[0] == "a")
	Combination2 = (s[len(s)-1] == "e")
	return Combination1 and Combination2

# 6. Write the function checkStartEndList(l) that takes a list consist of exactly 7 non-empty strings 
# and turns True if and only if the first, third, and fifth strings in the list all start with "a" and end with "e"
# please use the checkStartEndString function
# Example: In: l = ["apple pie", "banana", "apple","juice","apple juice","orange juice","coconut","coconut juice"]
#          Out: True
#          In: l = ["coconut","coconut juice", "apple pie", "banana", "apple","juice","apple juice","orange juice"]
#          Out: False
def checkStartEndList(l):
        return True

########## list ###########

# 7. Write a function calcList8, which takes in a list of 8 intergers: l1
# and returns another list l2 where 
# index 0 in l2 should now be the original first element in l1 raised to be power of 2
# index 1 in l2 should be the original second element in l1 raised to the power of 3
# index 2 in l2 should be set to 0
# index 3 in l2 should be set to 100
# index 4 in l2 should be set to the sum of the last 4 integers in the original list l1
# index 5,6,7 should copy the last 3 numbers in l1

# Example: In:  l1 = [1, 2, 3, 4,   5,  6, 7, 8]
#          Out: l2 = [1, 8, 0, 100, 26, 6, 7, 8]

def calcList8(l1):
	return (l1)

