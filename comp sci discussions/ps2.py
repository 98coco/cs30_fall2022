# 1. compare two numbers and return the larger one.
# You are not allowed to use max(a, b). 
# Make use of the if else statement.
#   Example input : a = 4, b = 5
#           return : 5

def larger_between_two(a,b):
        if a>b:
                return a
        elif a<b:
                return b
        else:
                return b
                
                
# 2. compare three numbers and return the largest.
# Make use of the larger_between_two function that you've already written.
#   Example input : a = 4, b = 5, c = 6
#           return : 6
def largest_among_three(a,b,c):
        if larger_between_two(a,b) < c:
                return c
        else:
                return larger_between_two (a,b)
        
# have to include (a,b) when nesting so that the function remembers what the argument is

#and is used when comparing whether two things are true // use for true or false
#or is used when comparing whether either or are true // use for true or false 

# 3. compare the numbers in the list and return the largest.
# This can be done through max(l), but try to do it with if else statement to check the length of list
# and reuse the larger_between_two or largest_among_three function
# The length of the list is assumed to be <= 3.
# For a list with only one element, just return that element. For empty list, return 0.
#   Example input : l = []
#           return : 0
#   Example input : l = [2]
#           return : 2
#   Example input : l = [2, 10]
#           return : 10

def largest_in_list(l):
       
        if len(l) == 2:
                a = l[0]
                b = l[1]
                return larger_between_two(a,b)
        if len(l) == 3:
                a = l[0]
                b = l[1]
                c = l[2]
                return largest_among_three(a,b,c)
        else:
                return 0

# for length you start counting from 1; only start counting from 0 when slicing and indexing
# have the labe a,b,c so that the if statement knows what a,b,and c are

# 4. [optional]
# You are hungry and are deciding what to cook. You only know three recipes, ordered by preference:
#    1. Hamburgers, which requires 2 pounds of ground beef and 2 slices of bread.
#    2. Peanut butter sandwich, which requires 1 ounce of peanut butter and 2 slices of bread.
#    3. Kabob, which requires 1 pound of ground beef and 3 onions.
# 
# Your job is to make a function that outputs what to cook given the available ingredients.
# It has the following signature:
# whatToCook(beef, peanutButter, bread, onions)
# - `beef` is an integer that gives the number of pounds of beef available
# - `bread` is an integer that gives how many slices of bread are available
# - `peanutButter` is an integer that gives how many ounces of peanut butter are available
# - `onions` is an integer that gives how many onions are available
# The function should return a string, either "Hamburger", "Peanut Butter Sandwich", "Kabob"
# depending on what you want to make (remember, make the things you prefer first!). 
# If none of these are possible, return "You are hungry!"
# Example input : beef = 1, peanutButter = 0, bread = 0, onions = 3
#		  return: "Kabob"
# def whatToCook(beef, peanutButter, bread, onions):
	# return "You are hungry!"




# For the rest of this worksheet, we will use recursion.


# 5. Given a list of integers l, return a list which doubles each element in the list
#   Example input : l = [1, 2, 3, 4]
#           return : [2, 4, 6, 8]

def doubleEachElement(l):
        if l == []:
                return []
        else:
                head = l[0]
                tail = l[1:]
                recursiveResult = doubleEachElement(tail)
                return [2*head]+recursiveResult 

# 6. Given a list of integers, return the sum of all even integers in the list.
# Replace "<???>" with code
#   Example input : l = [1, 2, 4]
#           return : 6

def sumEven(l):
        if l == []:
                return 0
        else:
                head = l[0]
                tail = l[1:]
                recursiveResult = sumEven(tail)
                if head % 2 == 0:
                        return head + recursiveResult
                else:
                        return recursiveResult

# 7. Remove the negative numbers in the list and return that list.
#   Example input : l = [1, -2, 3, -4]
#           return : [1, 3]

def filterNegativeNumbers(l):
	if l == []:
		return []
	else:
		head = l[0]
		tail = l[1:]
		recursiveResult = filterNegativeNumbers(tail)
		if head > 0 :
			return [head] + recursiveResult
		else:
			return recursiveResult

# can only compare integer to another integer and a list to another list (which is why l > 0 did not work -- you were comparing a list to an integer)
# u put  brcket around head in return becauase its a list and u r dding aa list to anaother list
