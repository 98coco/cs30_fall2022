# in lets us know whether smth is in a list

#returns true if element e is in the list 1; otherwise it returns false
#example: contains (5, [1,2,3]) returns False
#type of e: integer
# Type of l : list of integers
#type of result: boolean (Trueor False)

def contains(e,l):
    if l == []:
        return False
    else:
        head = l[0]  #1
        tail = l[1:] #[2,3]
        recursiveResult = contains(e,tail) # what should contains (5, [2,3]) return? False
        return e == head or recursiveResult

#dupList([1,2,3]) == [1,1,2,2,3,3]

def dupList(l):
    if l == []:
        return []
    else:
        head = l[0] #1
        tail = l[1:] #2,3
        recursiveResult = dupList(tail) # [2,2,3,3]
        return [head, head] + recursiveResult

'''

#dupList([1,2,3])
l = [1,2,3]
head = 1
tail = [2,3]
    dupList ([2,3])
    l = [2,3]
    head = 2
    tail = 3
        dupList ([3])
        l = [3]
        head = 3
        tail = [] 
            duplist[] --> return[]
            recursiveResult = []
            return [3,3]
            RecursiveResult == [3,3]
            return [2,2,3,3]
        recursiveResults = [2,2,3,3]
        return [1,1,2,2,3,3]

'''

#given a list of strings, return a lsit contaiang only the words of length 4 or more
#example: longWords(['python','programming','is','super','fun'])

def longWords(l):
    if l == []:
        return []
    else:
        head = l[0] # python type: string
        tail = l[1:] #['programming', 'is', 'super', 'fun'] type: string
        recursiveResult = longWords(tail) # ['programming' and 'super']; list of strings
        if len(head) >= 4:
            return [head] + recursiveResult
        else:
            return recursiveResult

 # put brackets around head because you are returning a string
 # max on recursion means that your created a loop

'''Common Errors

ALWAYS: Look at the last red lline and read it

* NameError: you are referring to a variable or function name that doesn't exist

*Type Error: You are passing the wrong type of aarguments to an operation
    (for example, trying to add an integer and a string)

*Recursion Error: your function runs forever. Check your reccursive call.
                Make sure that you recurse on the tail of the list.

* Type Error: longWords takes one positional argument but two were given.
    You are passing the wrong number or arguments to a function

*Index Error: Indexing into a list or string out of bounds
    examples: s = 'hello'
        s[17] causes and index error

*int is not subscriptable

You're using an int as if it's a string or list
    x= 3
    x[0]

'''

# recursion on numbers

# factorial

# factorial(n) = n * (n-1) *....*1

# factorial(n) = n * factorial(n-1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# What are the first two numbers multiplied together when we call factorial(5)
# What is actually happening?
# 5 *(4*(3*(2*(1*1))))


# use turtle.left & turtle.forward


#draw a equilateral triangle with each side of length sideLength

import turtle

def triangle(sideLength):
    #draw first side
    turtle.forward(sideLength)
    turtle.left(120)
    turtle.forward(sideLength)
    turtle.left(120)
    turtle.forward(sideLength)
    return


def triangle1(sideLength):
    #draw first side
    turtle.forward(sideLength)
    turtle.left(60)
    turtle.forward(sideLength)
    turtle.left(60)
    turtle.forward(sideLength)
    return

def triangle1(sideLength):
    #draw first side
    turtle.forward(sideLength)
    turtle.left(60)
    turtle.forward(sideLength)
    turtle.left(60)
    turtle.forward(sideLength)
    return

#not 60 because we aare using exterior angles when drawing

#spin to the left, turning 45 degree at a time
# n is the number of times to turn left

def spin(n):
    if n == 0:
        return
    else:
        spin(n-1)
        print('turned left') # <- way to test
        turtle.left(45)
        return

# order after else does not maatter in this situation but it other it might
# print statements can help w/ checking whether you are doing it correctly


#takes an item e and an integer n and creates a list with n copies of e in it
#for example: clone ('hello',3) returns ['hello','hello', 'hello']
#clone (True,5) returns ['True','True','True','True','True']
# type of e: T
# type of n: integer
# type of result: list

def clone(e,n):
    if n == 0:
        return []
    else: 
        recursiveResult = clone (e,n-1) #['hello','hello']
        return [e] + recursiveResult
        
        
# not using head and tail because head and tail are used for list
# n-1 is for numbers









    
