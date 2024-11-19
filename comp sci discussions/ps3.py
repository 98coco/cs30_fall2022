#------------------------------------------------#
#        part 1: short answers                   #
#------------------------------------------------#
# 1. I live pretty close to campus. Every morning I use the Python function below 
# to determine what mode of transportation to use to commute to work, based on how 
# many hours of sleep I got the previous night (argument sleep) and how many minutes 
# I have before my first meeting of the day (argument minutesForTravel).
def commute(sleep, minutesForTravel):
	if sleep < 7:
		return "car"
	elif minutesForTravel >= 60:
		return "walk"
	elif minutesForTravel >= 30:
		return "bike"
	else:
		return "car"

# (a) What is my mode of transportation when I’ve gotten 8 hours of sleep and have 
# 45 minutes until my first meeting?
# sol: 'bike'

# (b) Show a call to commute that returns the result "walk".
# sol: (8,80)

# (c) According to the commute function, under what conditions do I drive my car 
# to campus?
# (Choose the single best answer.) 
# i. when I’ve gotten fewer than 7 hours of sleep
# ii. when I have fewer than 30 minutes until my first meeting
# iii. when both of i and ii above are true
# iv. when at least one of i and ii above is true
# v. when exactly one of i and ii above is true

# sol: iv. when at least one of i and ii above is true

# is at least because if sleep < 7 it automatically gives car. However, it sleep < 7 is not true and it goes into the next line
# python will now analyze minutes of travel and if the persons travel is less than 30 mins then they need a car. At least on of
#these statements need to be true in order to get caar


# 2. Consider this function, where l is a list:
def mystery(l):
	if l == []:
		return []
	else:
		head = l[0] #[1]
		tail = l[1:] #[3,5]
	return mystery(tail) + [head]


#[5,3]+ [1]
   #[5]+[3]
     #[] + [5]

# mystery --> ([3,5)] + [1] ---> return [5,3,1]
# mystery --> ([5]) + [3] ---> return [5,3]
# mystery --> ([]) + [5] --> return 5

#calls:
        # 1c - mystery ([1,3,5])
        # 2c - mystery ([3,5])
        # 3c - mystery ([5])
        # 4c - mystery ([])
        


'''
recursion starts from the bottom up beccause the base case is when there is an actual value (0 or []) that will
help us figure out what to do for the recursion

'''

# (a) What does mystery([1,3,5]) return?
# sol: [5,3,1]

# (b) How many times is mystery called during the execution of mystery([1,3,5]), 
# including the initial call to mystery? (initial call - when you call the function)
# sol: 4 times 

# (c) What are the first two lists to be concatenated (using the + operator) 
# during the execution of mystery([1,3,5])? Make sure that your answer preserves 
# the order of the two arguments to the concatenation operation.
# sol: []+[5]

#concatenate means adding an element to a list



# 3. Consider the following function where x,y,z are numbers

def secret(x,y,z):
	if (x+y) > z:
		return x + y
	elif (x + z) > y:
		return x + z
	else:
		return z
# (a) What is the result of secret(2,5,6)

# sol: 7

# (b) What is the result of secret((1+3),1,7)
# (i) 8
# (ii) 5
# (iii) 11
# (iv) 7

# sol: iii


# 4. Consider the following functions where inp is a number and lst that is a list
def posQuadraple(inp):
	if inp > 0:
		return inp * 4
	else:
		return -1 * inp * 4

def greaterOfTwo(lst):
	if lst[0] > lst[1]:
		return lst[0]
	else:
		return lst[1]

# (a) What is the result of posQuadraple(greaterOfTwo ([-1,-2]))
# sol: 4

# (b) What is the result of posQuadraple(pow(greaterOfTwo([5,3]), 2))
# sol: 100

# the list in this case is [5,3]; 5 is greater than 3. We then get
#the squaare root of 5 becauase the equation says POW(greaterOfTwo([5,3]), 2)
# (remember we look at list first because its in the paranthesis)
# 25 * 4 == 100


#----------------------------#
#        part 3: if          #
#----------------------------#

# 5. The federal income tax plan currently being considered in Congress imposes
# a 12% tax on the first $37,500 of a person’s income, a 25% tax on all income 
# above $37,500 and less than or equal to $112,500, and a 35% tax on all income 
# above $112,500. For example, someone earning $30,000 would owe 
# 30,000 * 0.12 = $3600 in taxes, while someone earning $40,000 would owe 
# (37,500 * 0.12) + (2500 * 0.25) = $5125 in taxes. 
# Implement the function taxes that is declared below, which takes an income 
# (a number) as an argument and returns the taxes owed.

#type of income: integer

def taxes(income):
        if income <= 37500:
                return income * (12/100)
        elif income <= 112500: # you dont need 37500 < income because it has alr been applied at the first one
                                # return statement already covers having to multiply 37500 by 12%
                return (37500 * (12/100)) + ((income - 37500) * (25/100))
        return (37500 * (12/100)) + ((112500-37500) * (25/100)) + ((income - 112500) * (35/100))

# 6. You’ve been asked to implement a mini-calculator. The operators allowed 
# are +,-,*,/,%. . Implement a function miniCalculator that is declared below, 
# which two values x and y and a string operator op and returns the result of 
# x op y. e.g miniCalculator(3,1,’+’) returns 4.

def miniCalculator(x,y,o):
      if o == '+':
              return x + y
      elif o == '-':
              return x - y
      elif o == '*':
              return x * y
      elif o == '/':
              return x / y
      else:
              return x%y
        

#---------------------------------#
#        part 2: recursive        #
#---------------------------------#
# More mid-term practices: https://codingbat.com/python/List-2.

# 7. Write a function named q that checks that every number in a list that is 
# between 10 and 100 (inclusive) is even. Numbers outside this range may be in the list.
# For example, q([1,12,153,84,64,9]) returns True.

#type of input is a list
#type of output is a boolen value



def q(l):
       if l == []:
                return True
       else:
               head = l[0] #1 
               tail = l[1:] #12,153,84,64,9
               recursiveResult = q(tail) 
               if (evenN(head)) == True and recursiveResult == False:
                       return recursiveResult 
               elif (evenN(head)) == False and recursiveResult == True:
                       return evenN(head)
               elif (evenN(head)) == False and recursiveResult == False:
                       return evenN(head)
               else:
                       return True
               
def evenN(n):
        if n >= 10 and n <= 100:
                return n%2 == 0
        elif n<10 or n>100:
                return True #return true because there can be values outside the range that are even (we are only focusing on inside the range)
        else:
                return False
                
      

# 8. Write a function named minimum that returns the smallest element in a list 
# of integers.  If the list is empty, return math.inf.
import math

# input: list of integers
# output: integer (smallest element)

def minimum(l):
        if l == []:
                return math.inf
        else:
                head = l[0]
                tail = l[1:]
                recursiveResult = minimum(tail)
                if head > recursiveResult:
                        return recursiveResult
                if head < recursiveResult:
                        return head


# 9. Write a function named tails that takes a list and returns a list of 
# lists containing the original list along with all tails of the list, from 
# longest to shortest.  For example, tails([1,2,3]) is [[1,2,3], [2,3], [3], []],
# and tails([]) = [[]].

# input: list
# output: list of list


def tails(l):  #([1,2,3])
        if l == []:
                return [[]]
        else:
                head = l[0] #1
                tail = l[1:] # 2,3 
                recursiveResult = tails(tail) # [[2,3], [3], []]
                return [l] + recursiveResult

# 10. Write a function named flatten that takes a list of lists and flattens it 
# into a single list.  For example, flatten([[1,2], [3], [], [4,5,6]]) returns 
# [1,2,3,4,5,6].
def flatten(l):
        if l == []:
                return []
        else:
                head = l[0]
                tail = l[1:]
                recursiveResult = flatten(tail)
                return head + recursiveResult
       #head is alr a list so u dont need to add brackets

#----------------------------#
#          ADVANCED          #
#----------------------------#

# 11. Write a function named rmDups that removes consecutive duplicates from a 
# list. For example, rmDups([1,2,2,3,3,3,4,2,2,3]) returns [1, 2, 3, 4, 2, 3].
def rmDups(l):
	return []


# 12. Check if the input l(can be a string or a list) is a palindrome with the recursive function isPalindrome.
# The function returns True if the input is a palindrome. For example, isPalindrome([1, 2, 2, 1]) returns True.
# isPalindrome("abba") returns True. isPalindrome("abbc") returns False.
def isPalindrome(l):
	return False

# 13. Write a function multiplyAllByFirst that takes a list of numbers and 
# returns a new list where each number is multiplied by the first one in the list.  
# For example, multiplyAllByFirst([4, 0, 2, 5]) = [16, 0, 8, 20].
# Your code has to work on emtpy list as well. if input list is empty then you should return an empty list
def multiplyAllByFirst(l):
	return []
