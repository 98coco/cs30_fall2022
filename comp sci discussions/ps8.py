import functools

# += means adding  to result and it being equal to result


#--------------------- dictionaries -----------------------

# Video games often track player attributes using something like a dictionary.
# A *player map* p is a dictionary that has the following entries:
#   p["score"]: the current player's score, a non-negative integer
#   p["location"]: the player's location,
#           given as a dictionary with entries for "x" and "y" coordinates that are both integers.
#   p["health"]: the player's health, given as an integer between 0 and 100
#   p["name"]: the player's name, given as a string.
# For instance, an example player map is:
#  joeBruin = {"score": 1000, "location": {"x": 0, "y": -10}, "health": 50, "name": "Joe Bruin"}

# 1. Write a function that greets the player by returning "Hello, {player name}!"
#    (replace {player name} with their name) if they are alive (health
#    greater than 0), or returns "You are Dead!" if they are dead.
# Example: greetPlayer(joeBruin) returns "Hello, Joe Bruin!"

def greetPlayer(p):
    if p["health"] > 0:
        print ("Hello, " + p["name"] + "!")
    else:
        print ("You are Dead!")

# 2. All active players (health > 0) with scores >= s will be teleported to the final destination (x, y)
# Write a function movePlayer(p, x, y, s) that takes in player p, final destination x, y, and score requirement s 
# returns a new player that is equivalent to the old one except at the final position (x, y), if he or she is eligible to be teleported
# if not eligible just return the old player as it is

# joeBruin  = {"score": 1000, 
#              "location": {"x": 0, "y": -10}, 
#              "health": 50, 
#              "name": "Joe Bruin"}

# janeBruin = {"score": 20, 
#              "location": {"x": 0, "y": -10}, 
#              "health": -1, 
#              "name": "Jane Bruin"}

# Example: movePlayer(joeBruin,  500, 500, 1000) ==> {'score': 1000, 'location': {'x': 500, 'y': 500}, 'health': 50, 'name': 'Joe Bruin'}
# Example: movePlayer(janeBruin, 500, 500, 1000) ==> {'score': 20, 'location': {'x': 0, 'y': -10}, 'health': -1,'name': 'Jane Bruin'}

def movePlayer(p, x, y, s):
    if p["health"] > 0 and p["score"] >= s:
        return {"score": p["score"], "location":{"x": x, "y": y} ,"health": p["health"], "name": p["name"]}
    else:
        return p

# 3. Consider the dictionary: imaginary_number = {"real": a, "im": b}, where a and b are integers and is equivalent to a + bi. a,b != 0
#    Given a list of imaginary numbers write a function that returns the list of imaginary numbers multiplied by i
#    Input : [{"real": 1, "im": 2}, {"real": -1, "im": -4}]
#    Expected Output: [{"real": -2, "im": 1}, {"real": 4, "im": -1}]
#    Feel free to define a function!
# (1 + 2i) * i == -2 (new real part) + 1i (new imaginary part)
# i * i == -1
# i * n == ni

def multiplyByi(rationals):
    return list(map(lambda x:{"real": x["im"] * -1, "im": x["real"]},rationals))


#----------------------- for loops -------------------------

# 4. Write a function to count the number of integers in l that contains a digit 7.
#    Hint: an integer i can be converted to a string with str(i).
#    Example: count_7([1,17,72]) returns 2.

def count_7(l):
    result = 0
    for number in l:
        if '7' in str(number):
            result = result + 1
    return result
  
# 5. Write a function to calculate the sum of following series: 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n
#    n is an input which is assumed to be positive. 
#    Example: series(4) -> 2.083 (1 + 1/2 + 1/3 + 1/4 ~= 1+0.5+0.333+0.25)
#    Note: round your result to three decimal places with round(result, 3)

def series(n):
    result = 0
    for x in range(1,n+1): #range does not return a list by default, but here it will!
        recip = 1/x
        result = result + recip
    return round(result,3)


# 6. Write a function to create the multiplication table (from 1 to 10)
#    of a number n and returns a list. 
#    Input: 6
#    Expected Output: [6,12,18,24,30,36,42,48,54,60]
def multTable(n):
    result = []
    for x in range(1,11):
        result = result + [n*x]
    return result

# 7. Consider the dictionary: rational = {"num": a, "denom": b}, where a and b are integers. b != 0
#    Given a list of rationals write a function to return the maximum value
#    Input : [{"num": 1, "denom": 2}, {"num": 1, "denom": 4}]
#    Expected Output: {"num": 1, "denom": 2}
def maxRationals(rationals):
    return {}

#------------------- more dictionaries and loops practice (do on your own time) -------------------

# Consider the following list of search results retrieved when looking up
# how to make a Thanksgiving dinner:
searchResults = [
    {"title": "The Perfect Cranberry Sauce", "keywords": ["cranberries"], "relevance": 25},
    {"title": "Roasting a Turkey: 101", "keywords": ["bird"], "relevance": 88},
    {"title": "How Not to Ruin Thanksgiving", "keywords": ["social gathering", "thanksgiving"], "relevance": 25},
    {"title": "How to Bake a Pie", "keywords": ["baking", "pie"], "relevance": 9},
    {"title": "One Hundred Things Your Uncle Shouldn't Say at Thanksgiving",
     "keywords": ["inappropriate behavior", "thanksgiving"], "relevance": 1},
    {"title": "How To Stuff a Turkey", "keywords": ["turkey", "stuffing", "baking advice"], "relevance": 88},
]
# Write functions that use map, filter, and reduce to compute the following
# quantities (where the list of search results is given as an argument). You
# can use the above list of search results as a test case, but feel free to
# modify it to get more tests.

#not sure what htis is asking?? ask in ofh



# 8. Find the highest relevancy score in the search results.

def getOneRelevance(r): # r = one dictionary 
    return r['relevance'] 

def findGreatestRelevanceMap(results): 
    allRelevances = list(map(lambda x: getOneRelevance(x),results))
    return max(allRelevances)


# 9. Return the list of the title of all the search results with the greatest relevance.

def findNamesOfGreatestRelevance(results):
    highestRelevance = findGreatestRelevanceMap(results)
    dictionaries = list(filter(lambda x: True if x['relevance'] == highestRelevance else False, results))
    return list(map(lambda x: findOneName(x),dictionaries))

def findOneName(r):
    return r['title']

# 10. This problem references the searchResults list from problems 3 and 4.
# First restrict the search space to titles with "thanksgiving" as keywords 
# then find the list of the titles of the most relevant search results  
# For example: mostRelevantWithThanksgiving(searchResults) == ['How Not to Ruin Thanksgiving']

def findOneKey(r):
    return r['keywords']

def mostRelevantWithThanksgiving(results):
    thingsWThanks = list(filter(lambda x: True if 'thanksgiving' in findOneKey(x) else False,results))
    return findNamesOfGreatestRelevance(thingsWThanks)
    

# 11. This problem references the searchResults list from problems 3 and 4.
# Return the average length of the titles of all article with relevance at least
# as great as some constant k (given as an argument).


def averageLengthAbovek(results,k):
    return [] 


# 12. Write a function isPrime to identify if a given number is prime 
#    (A prime number (or a prime) is a natural number greater than 1 
#    that has only two factors: 1 and n.)
#    Hint: check all possible numbers that can divide n
#    Input: 11
#    Expeted Output: True


def isPrime(n):
    res = False
    i = 2
    while i < n:
        if n%i != 0:
            res = True
        else:
            return False
        i += 1
    if n == 2:
        res = True
    return res


# 13. Write a function getPrimes to return a list of primes between 2 and n.
#    Please use isPrime defined above.
#    Input : 10
#    output : [2,3,5,7]
def getPrimes(n):
    res = []
    ListOfNums = list(range(n+1))
    for i in ListOfNums:
        if isPrime(i) == True:
            res += [i]
        else:
            res
    return res

# 14. Write a function that return a string in a triangle pattern with a pre-defined 
#    number of rows. 
#    Hint: use "\n" to make a new line
#    Example: If we print the result string of draw(4), it will display like the following in the scetion betwenn two """:    
"""
#
##
###
####
"""
def draw(n):
    return

import functools

# 15. Given a list of list, return the max number of each inner list.
#    Each inner list is not sorted. You are not allowed to use the max function.
#    Try to do it with the for loop.
#    Input: [[1,2,3], [7,2,3], [8,10,9]]
#    Expected output: [3, 7, 10]

def maxOneList(l):
    return max(l)

def maxOfInnerListLoop(lists):
    res = []
    for x in lists:
        res += [maxOneList(x)]  
    return res

def maxOfInnerListRecursion(lists):
    if lists == []:
        return []
    else:
        head = lists[0] #[1,2,3]
        tail = lists[1:] # [[7,2,3], [8,10,9]]
        return [max(head)] + maxOfInnerListRecursion(tail)
        
def maxOfInnerListReduce(lists):
    return functools.reduce(lambda pr, curr: pr + [maxOneList(curr)],lists,[])


    






















