
'''
For Loop

for x in e:
    <statements>


x is a variable name (can be anything)
e is an expression that evaluates to a list
statements will be executed once per element of the list
    - that element is given the name x

'''

#summing the elements of a list using loops

def sumList(l):
    result = 0  #accumulator variable
    for x in l: 
        result = result + x
    return result

''' General approach to iteration:

- introduce an "accumulator" variable (result in our cse above)
- initialize the accumulator to the result if the list is empty
- what goes inside the loop?
    - consider an arbitrary element x of the list
    - assume the accumulator contains the right answer for the prefix of the list up to x  
    - inside the loop, update the accumulator to take x into account
    - acumulator kinda like partial result in reduce and x is kinda like curr elem in reduec

'''


import math

def minimum(l):
    result = math.inf
    for x in l:
        if x < result:
            return x
    return result  # we r done w/ the function have to have the return outside the loop to end the loop

def minimum2(l):
    m = l[0]
    for x in l:
        if x < m:
            m = x
    return m  #after the for loop is done


# True if all elements of l are even and False otherwise 


def allEven(l):
    for x in l:
        if x%2 == 1:
            return False
    return True


def allEven2(l):
    result = False
    for x in l:
        if x % 2 == 1:
            return False
        else:
            result = True
    return result


#hasElemEqualToIndex([3,5,2,5,6]) = True ( 2 is the same as the index it is at which is l[2])

def hasElemEqualToIndex(l):
    i = 0  # i is the index
    for x in l:
        if i == x:
            return True
        i = i + 1
    return False 


def hasElemEqualToIndex2(l):
    for i in range(len(l)): # this is the indexes of l
        if i == l[i]:
            return True
    return False



def factorial(n):
    result = 1
    for x in range(1, n+1): # need the plus one -- if n = 5 then you will only get the list 1,2,3,4 if u dont add one; to get 1,2,3,4,5 add 1
        result = result * x
    return result

#doubleAll([1,2,3]) = [2,4,6]

def doubleAll(l):
    result = []
    for x in l:
        result = result + [x*2]
    return result

#return positives([2, 4, -2, 0, 3]) = [2,4,3]

def positives(l):
    result = []
    for x in l:
        if x > 0:
           result = result + [x]
    return result
        

#indexofMin([3,5,2,6,-2]) returns 4 

def indexofMin(l):
    m = math.inf
    for x in l:
        if x < m:
            m = x
    i = -1 # adding -1 bc when u enter the loop it starts indexing at 0
    for x in l:
        i = i + 1  
        if x == m:
            return i 

            
def indexofMin2(l):
    i = 0
    m = math.inf
    mIndex = -1
    for x in l:
        if x < m:
            m = x
            mIndex = i
        i = i + 1
    return mIndex  

    
def indexofMin2(l):
    m = math.inf
    mIndex = -1
    for i in range(len(l)):
        if l[i] < m:
            m = l[i]
            mIndex = i
    return mIndex
        
















