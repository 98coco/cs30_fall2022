
#double all elements of a list

def doubleAll(l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        recursiveResult = doubleAll(tail)
        return [head * 2] + recursiveResult

#add an exclamation mark to all strings in the lsit

def exclaimAll(l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        recursiveResult = exclaimAll(tail)
        return [head + '!'] + recursiveResult

#python codifies this common patterns, of walking through a list and creating
# a new list that is like the original but with each element transformed in some way


#function is called map (always tell map what to do -- if u want a list you have
# to say list(map) and then the function; less chances for error and allows for the code to be more readable

#all u have to do is figure out what u are doing to the input

#map uses the function/passes the function

#ex: list(map(doubleOdd,l))-- doubleOdd is the function and map applies that function to the list l
#we need list in front of map or whatever we want in front of map for the problem to go thru


#relies on the ability for functions to take other functions as arguments


def double(n):
    return n * 2

def exclaim(s):
    return s + '!'

def doubleAllUsingMap(l):
    return list(map(double, l))

def exclaimAllUsingMap(l):
    return(map(exclaim,l))

#takes a list of strings and returns a list of the lengths
#stringsToLength(['hello', 'joe']) returns [5,3]

def stlHelp(s):
    return len(s)
    

def stringsToLength(l):
    return list(map(stlHelp,l))

def stringsToLength(l):
    return list(map(len,l))

#return a lsit of integers like the given list but where all odd lements are doubled
#doubleOdds([1, 0, 4, 5, 3]) = [2, 0, 4,10,6]

def doubleOdd(n):
    if n%2 != 0:
        return n * 2
    else:
        return n

def doubleOdds(l):
    return list(map(doubleOdd,l))


#another common pattern: walk through a list and return  new list containing a subset of the elements


# evens ([1, 0, 3, -2, 4, 5]) returns [0, -2, 4]

#largeStrings(['hello', 'there', 'how', 'are', 'you', 'today]) returns
# ['hello', 'there', 'today']


#Python's filter funtion supports this pattern
# - like map, filter takes a function and a list
# but the function argument is different
#  - takes a list element as an argument
#  - returns True or False (true means to return this element, false means dont return)


def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False 

def evens(l):
    return list(filter(isEven,l))


def isLargeStrings(s):
    if len(s) >= 4:
        return True
    else:
        return False

def largeStrings(l):
    return list(filter(isLargeStrings, l))


def true(s):
    return True

#keeps every element

def false(s):
    return False
 
#takes out every element


#remove all even numbers from a list and double all the odd ones
#f([1, 5, 6, 2, 3]) = [2,10,6]

def fHelp(n):
    if n%2 != 0:
        return True
    else:
        return False



def f(l):
    #remove all the evens from the list l
    noEvens = list(filter(fHelp,l))
    return list(map(double,noEvens))


#We can define map and filter ourselves
#map is applying the function we give it to the head


def myMap(f,l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        recursiveResult = myMap(f, tail)
        return [f(head)] + recursiveResult


def myFilter(f,l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        recursiveResult = myFilter(f, tail)
        if f(head) == True:
            return [head] + recursiveResult
        else:
            return recursiveResult
            


#anonymous function - a function with no name

#lambda is declaring  a function (once you call it you can throw it away)
#lambda is used for convenience
#allows us to use map and filter without having to define another function
#lambda is restrictive in python to line of code

# ex:  list(map(lambda n:n*2,[1,2,3,4])) <-- doubling n

#calling lambda; you need lambda it defines the argument such as n

#(lambda n: n*2)(45)
#90
#(lambda x.y: x * x + y)(3,4) <-- using lambda for multiple arguments



def doubleAll2(l):
    return list(map(lambda n: n * 2,l))


def exclaimAll2(l):
    return list(map(lambda s: s + '!',l))


def evens2(l):
    return list(filter(lambda n: n%2 == 0,l)) #l means you are applying the function on the list


#if expression in lambda

#EX: return a list of integers like the given list but where all odd lements are doubled
#doubleOdds2([1, 0, 4, 5, 3]) = [2, 0, 4,10,6]

# lambda n: n if n % 2 == 0 else n*2 (how to write lambda w/ if statement)
# Python has an "if" expression, which is useful inside lambda since the body
# of a lambda must be a single expression

def doubleOdds2(l):
    return list(map(lambda n: n if n % 2 == 0 else n*2,l)) # <-- if expression 

#you can't use elif for lambda but you can nest them with each other


# difference between expression & statement:

#two categories of syntax in programming languages -

#an *expression* is something that evaluates to a value (i.e. some data)
#example: 1 + 1, 1>5, f(24)
# True if x>0 else False <-- expression because it is giving us a value; the value is true

#a *statement* (or a command) is just an action that the computer takes but
#doesn't evaluate to any value
#example: x = 54, return statements and if statements


#a lambda can refer to any variables that are available in the surrounding scope
#example: generalize doubleAll so thaat we multiply each element of a list by
#some number c

# multiply the list by the integer c

def multAllBy(c, l):
    return list(map(lambda n: n * c,l))


import functools


#reduce(f,l,b)
# b = base is the base case value - the value to return if l ==[]
# l = list is the list that I want to traverse
# f = function takes two arguments:
#   the second argument is an element of the list l
#   the first argument is the partial result obtained so far

#example : functools.reduce(lambda x, y: x + y,[1,2,3,4],0)
# is doing the following computation:
# ((((0+1) + 2) + 3) + 4)
# 0 is the base case value, 1 is the first partial result, then 3, then 4, then 6, then the totl is 10



def factorial(n): #n =5 
    l = list(range(1, n+1)) #[1,2,3,4,5]
    return functools.reduce(lambda x,y: x*y, l, 1)

import math

#when using reduce, you will need two arguments x and y; allows for comparison


def minimum(l):
    return functools.reduce(lambda x,y: min(x,y),l, math.inf)

def minimum2(l):
    return functools.reduce(lambda x,y: x if x < y else y,l, math.inf)

# y represents some element of the list
# x is the current element we are comparing to y


def myreduce (f,l, partialResult):
    if l == []:
        return partialResult
    else:
        head = l[0]
        tail = l[1:]
        newPartialResult = f(partialResult,head)
        return myreduce(f, tail, newPartialResult)
        
# for this recursion we are computing on the way down rather than on the way up


#returns True if l contains an even number; otherwise returns False 
# type of l is a list of number
# type of result is a boolean



def containsEven(l):
    # type of y is a int (it is and element of the list)
    # type of x is a boolean (because x is always a partial result -- have we seen an even number so far)
    return functools.reduce(lambda x,y: x if y%2 != 0 else True, l, False)

# x is false until you find one element that is even; we assume x if false bc we assume tht
# an element is not even until we see that it is

# not saying functools.reduce(lambda x,y: True if y%2 == 0 else False, l, False) because it is ignoring partialResult
# partialResult gives us the answer from the beginning of the list; without the partialResult, we can't recurse.
# Once we hit the last element of  the list if it is odd and previous numbers haave been even
#it will give us false (for the last element) since we are ignoring the partial result


def containsEven2(l):
    # type of elem is a int (it is an element of the list)
    # type of partialResult is a boolean (because x is always a partial result -- have we seen an even number so far)
    return functools.reduce(lambda partialResult,elem: partialResult or elem%2 == 0, l, False)


# ^^^ helps explain reduce/lamba better (the elem and partialResult)
#use base case first from the list as partial result
                
