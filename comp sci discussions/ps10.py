import functools

# Part 1: For loop/mutation exercises
# Solve each of these problems using for loops (no recursion or map/filter/reduce)
# Hint: you may want to use a dictionary

# 1. Sometimes people have a preferred name that they would rather use instead of
# their given name. Write a function greetPreferredName(givenNames, preferredName) that given a list of
# strings "givenNames" and dictionary "preferredName" that maps given names to preferred names,
# prints "Hello (preferred name)!" for each person. If there is no preferred name, simply
# greet with the given name.
# The function should not return anything, and should print the names in the order that they appear in the givenNames list.
# Example:
# greetPreferredName(["william", "disha", "todd"], {"william": "will", "todd": "the toddster"}) prints:
# Hello will!
# Hello disha!
# Hello the toddster!

# preferredName['william'] == will


def greetPreferredName(givenNames, preferredName):
    for x in givenNames: # ["william", "disha", "todd"]
        if x in preferredName.keys():
            print ('Hello', preferredName[x], '!') # dont need quotation on x for dictionary bc x alr has quotation; ex:  x = 'william'
        else:
             print ('Hello', x, '!')

def greetPreferredName2(givenNames, preferredName):
    for x in givenNames: # ["william", "disha", "todd"]
        if x in preferredName:
            print ('Hello', preferredName[x], '!') 
        else:
             print ('Hello', x , '!')


# 2. Write a function printOnce(l) that prints each element of the list on a
# separate line, while skipping duplicates. The elements should be printed
# in the order that they appear in the list.
# Example:
# printOnce([1, 3, 2, 1, 4, 2]) prints:
# 1
# 3
# 2
# 4

# make a new list or dictionary(with no duplicates) and then print the new list

def printOnce(l):
    dictionary = {}
    for n in l:
        if n in dictionary:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    for key in dictionary:
        print(key)

def printOnce2(l):
    accum = []
    for x in l:
        if x not in accum:
            print(x)
            accum += [x]
 
        
# 3. Write a function findMostFrequent(l) that finds the most frequent element in
# a list. Assume that there is a unique most common element.
# Example: findMostFrequent([1, "hello", 3, 3, 3, 1, 8, 4]) == 3

# want to keep track of wat is being repreated

def findMostFrequent(l):
    counter = {}
    #creates a dictionary and counts freq for each elem
    for x in l:
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1
    max = counter[l][0]
    max_key = l[0]
    #for every value in dictionary, if thats the max then we set the max value and key
    for x in counter:
        if counter[x] > max:
            max = counter[x]
            max_key = x
    return max_key 



# 4. What will these two functions return?
# Will the following two functions return the same thing? Why or why not?
# Do this without running the functions. 

def mystery1():
    a = 3
    b = 4
    x = [a, b] #x = [3,4]
    l = [x, 5] # l = [[3,4], 5]
    a = 5  # x = [3, 4]  # x is still pointing at 3,4 (ur not changing the a in x only the a outside)
    return l # l = [3,4],5] # because only a changes and doesnt change x


def mystery2():
    a = 3
    b = 4
    x = [a, b] # x = [3,4]
    l = [x, 5] # l = [[3,4],5]
    x[0] = 5  # x = [5,4]
    return l #[[5,4],5]

##############################################################################################

import functools
import math

# Part 2: General Review
# Separately solve each of these problems using loop, map/filter/functools.reduce, and recursion

# 5. Write a function average that takes a non-empty list of numbers and returns their average.
#    you can use the built-in function len() but please dont use the sum() function


#loop version:

def averageLoop(l):
    res = 0
    for x in l:
        res += x
    return res/len(l)

#reduce version:

def averageReduce(l):
    sumL = functools.reduce(lambda pr,curr: pr + curr, l, 0)
    return sumL/len(l)

#recursion version:
#when doing recursion keep in mind of ur base case and what u r returning ok!!!!

def averageRecur(l):
    return sumList(l)/len(l)

def sumList(l):
    if len(l) == 1:
        return l[0]
    else:
        head = l[0]
        tail = l[1:]
        return head + sumList(tail)


# 6. Write a function noZeroLists that takes a list of lists and removes any
#    inner lists that contain at least one 0 in them.
#    For example, noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]])
#    returns [[1,2,3], [], [1,1,1]].
#    Hint: Python's "in" operator for checking whether a value is in a list will be useful.

#loop version:

def noZeroListsLoop(l):
    accum1 = [] 
    for x in l: #one list in l
        if 0 in x:
            accum1
        else:
            accum1 += [x]
    return accum1

#filter version:

def noZeroListsFilter(l):
    return list(filter(lambda x: True if 0 not in x else False, l))

#reduce version: remember that for reduce pr comes first

def noZeroListsReduce(l):
    return functools.reduce(lambda pr, curr: pr + [curr] if 0 not in curr else pr, l ,[])

#recursion version: keep in mind ur base case bessie!! 

def noZeroListsRecurse(l):
    if l == []:
        return []
    else:
        head = l[0] #[1,2,3]
        tail = l[1:] #[4,0,5], [], [1,1,1], [0,1,2] < -- assume this gives us [],[1,1,1]
        if 0 in head:
            return noZeroListsRecurse(tail)
        else:
            return [head] + noZeroListsRecurse(tail)


# 7. Write a function innerMultiply that multiplies all elements of a list of lists
#    by a given number.  For example, innerMultiply([[1,2,3], [4,5]], 10)
#    returns [[10,20,30], [40,50]].

# loop version // do we need nested loop for when we need to manipulate things in the innerlsit

def innerMultiplyLoop (l,e):
    accum1 = []
    for x in l: #[1,2,3]
        accum2 = []
        for y in x: #[1]
            accum2 += [y*e] #be careful about the variables you are using
        accum1 += [accum2]
    return accum1
            
# map version:

def innerMultiplyMap (l,e):
    return list(map(lambda x:list(map(lambda y: y * e,x)),l))

def innerMultiplyMap2 (l,e):
    return list(map(lambda x: innerMultiplyOne(x,e),l)) #keep in mind how many arguments your helper function is taking in 

def innerMultiplyOne (l,e):
    return list(map(lambda x: x * e,l))

# reduce version: # remember to return a base case for reduce

def innerMultiplyOneR (l,e):
    return functools.reduce(lambda pr, curr: pr + [curr * e], l,[])

def innerMultiplyReduce (l,e):
    return functools.reduce (lambda pr, curr: pr + [innerMultiplyOneR(curr,e)],l,[]) 

#recursion version:


def innerMultiplyRecurse (l,e):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        return [innerMultiplyRecurseOne(head,e)] + innerMultiplyRecurse(tail,e)

def innerMultiplyRecurseOne (l,e):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        return [head * e] + innerMultiplyRecurseOne(tail,e)

    #remember when having two arguments for recurse, u need to add the second argument to the tail to go back again
    

# 8. Write a function named q that checks that every number in a list that is
#    between 10 and 100 (inclusive) is even.
#    For example, q([1,12,153,84,64,9]) returns True.


#for loop version:

def qLoop(l):  
    res = False 
    for x in l:
            if x >= 10 and x <= 100:
                if x%2 == 1:
                   res = False
                else:
                    res = True
            else:
                res 
    return res
                

#filter version

def qFilter(l):
     newList = list(filter(lambda x: False if 10 <= x <= 100 and x%2 != 0  else True,l))
     return True if newList == l else False


#reduce version:

def qReduce(l):
    return functools.reduce(lambda curr, pr: True if 10 <= curr <= 100 and curr%2 == 0 else pr, False,l)



# 9. Professor Puzzler is a crossword enthusiast. She has a long list of words that might appear
#    in a crossword puzzle, but she has trouble finding the ones that fit a slot.
#    Write a function crosswordFind to help her.
#    The expression crosswordFind(letter, inPosition, length, words)
#    should return all the items from the list words which 
#    (a) are of the given length
#    (b) have letter in the position inPosition.
#    For example, if Puzzler is looking for seven-letter words that have 'k' in position 1,
#    she can evaluate the expression:
#    crosswordFind('k', 1, 7, ["funky", "fabulous", "kite", "icky", "ukelele"])
#    which returns ["ukelele"].


def crosswordFind(letter, inPosition, length, words):
    words = list(filter(lambda x: len(x) == length,words))
    return list(filter(lambda x: x[inPosition] == letter, words))



# 10. Write a function that checks the validity of a password. 
#    for a password to be valid, it has to have: 
#    At least 1 letter between [a-z, A-Z]
#    At least 1 number between [0-9]
#    At least 1 character from [$#@]
#    for example checkPassword("ab01") should return False as it doesnt contain any special character
#    Important Rule: You are not allowed to use the built-in function "in" to check presence of certain character.  
#    Instead, just visit each character in the given string one by one with loop, functools.reduce or recursion. 
#    hint: ord() might be useful 


def checkPasswordLoop(p): #<-- wrong
    res = False
    resLetter = False
    resNum = False
    resSpec = False
    for i in range(len(p)):
        if 97 <= ord(p[i]) <= 122 or 65 <= ord(p[i]) <= 90:
            resLetter = True
        elif '0' <= p[i] <= '9':
            resNum = True
        elif p[i] == '$' or '#' or '@':
            resSpec = True
    if resLetter == True and resNum == True and resSpec == True:
        res = True
    else:
        res    
    return res
        
