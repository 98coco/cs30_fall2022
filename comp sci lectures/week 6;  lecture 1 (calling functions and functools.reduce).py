
# you can pass functions as other functions (ex: minimum)

def minimum(lessThan,l):
    if len(l) == 1:
        return l[0]
    else:
        head = l[0]
        tail = l[1:]
        recursiveResult = minimum(lessThan,tail)
        if lessThan(head,recursiveResult):
            return head
        else:
            return recursiveResult

#lessThan is a function
#this function can be used for finding the minimum of strings alphabetically and by len
# minimum(lambda s1, s2: len(s1)< len(s2),['everyone','out','hello']) returns 'out' <=== len
# minimum(lambda s1, s2: s1 < s2,['everyone','out','hello']) returns 'everyone' <==== alphabetical


#example: richest customer([[30,50],[100,10],[60,60]]) == [60,60]

def richestCustomer(l):
    return minimum(lambda a1,a2: a1[0] + a1[1] > a2[0] + a2[1] ,l)
    

import turtle

def drawingApp():
    # go forward 25 steps when the 'f' key is pressed
    turtle.onkey(lambda: turtle.forward(25),'f')
    

# functions can return other functions

# example: automatic differentiation

#derivative of: x^2 + 2x +5 --- 2x+2
#lim (h -> 0) (f(x+h) - f(x))/h

def derivative(f):
    h = 0.00000001
    return lambda x: (f(x+h) - f(x))/h
    
# give it a function
# f = lambda x: x*x +2*x+5
# fPrime = derivative(f) <-- have to give it a function
#derivative is a function and returns a function


import functools

'''
functools.reduce(lambda x,y: x +y, [1,2,3,4,5,6],0)

((((((0+1)+2)+3)+4)+5)+6) = 21

'''

def myreduce(f,l,partialResult):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        newPartialResult = f(partialResult,head) # add 0 to 1
        return myreduce (f,tail,newPartialResult) #newPartialResult becomes the new "base"

#example: duplicateAll([1,2,3]) = [1,1,2,2,3,3]
#type of l: list of integers
#type of result: list of integers
#type of y(currElem) is an integer because it is a current element of a list
#type of x (partialResult) is a list of integers aka base case
    
def duplicateAll(l):
    return functools.reduce(
        lambda partialResult, currElem: partialResult + [currElem,currElem],
        # type of currElem is an integer -- some element in the list
        #type of partialResult is a list of integer -- partialResult is the list alr made
        l,
        [])


#incrementAll([1,3,5]) = [2,4,6]

def incrementAll(l):
    return functools.reduce(lambda x,y: x+[y+1], l,[])

#y is the current element (what is in the list so it is an integer)
# x is the partial result (list of integers)
#assume paartil result alr did what we want it to do

'''
((([]+[1+1]) + [1+3]) + [1+5]) 

'''


#reverse([1,3,5]) = [5,3,1]

def reverse(l):
    return functools.reduce(lambda x,y: [y]+ x ,l,[])

'''

(((1+[]) + [3,1]) + [5,3,1])

'''

# removeOddsAndHalvesEven([1,5,4,8,21] = [2,4]
 
def removeOddsAndHalvesEven(l):
                                        #[2]          8         
    return functools.reduce(lambda partialResult,currElem: partialResult + [currElem//2] if currElem%2 == 0 else partialResult, l,[])


#assume partialResult already gives you what you want

#when currElem = 8 we expect to get 4
        

