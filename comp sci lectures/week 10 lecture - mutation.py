
def update(newL):
    newL[2] = 8
    return newL

'''

l = [5,6,7]
anotherList = update(l)
anotherListreturns [5, 6, 8]


^^ this is rlly weird and a type of mutation in programming

'''


# w/ a variable it just holds the address of what we want to reference; pointing to a memory 
# EX: x = 42
# x holds to reference/ address to 42
# x = 43 
# x still holds the memory of 42 but rather then giving us 42 it points to 43 and gives us 43

# COPY 
# y = x
# y is copying x's address its address so now it points to 43
# 
#y and x are aliases


#The only things you need to understand, in order to understand any piece of code in terms of how 
#it handles mutation:

#keypoint 1: variables always hold references to data, rather than the data itself (reference is the address - memory location)
#keypoint #2: copying a variable always copies the reference, not the data (reference is the address - memory location)


#you can't really delete data in most languages so you just reassign things

# a lot of errors occur because of mutations to list or variables


def doubleAll(l):
    accum = []
    for x in l:
        accum += [2*x] #not overriding the variable l and is going into accum instead so l remains the same
    return accum


'''
on playground:

l = [1,2,3]
l2 = doubleAll(l)
l2
[2, 4, 6]
l
[1, 2, 3]

'''

def doubleAll2(l):
    for i in range(len(l)):
        l[i] = l[i] * 2  #overriding smth to a variable // in place update
    return l

''' mutation in affect 

l = [1,2,3]
l2 = doubleAll2(l)
l2
[2, 4, 6]
l
[2, 4, 6] #this is occuring because you are manipulating an element in the variable l 

''' 


#swap([1,3]) = [3,1]
#no mutation / no swap pair 

def swap(p):
    return [p[1],p[0]]

#create an inplaceswap that changes the variable

#updates the given list in place to the swap
#order of elements

def inPlaceSwap(p):
    oldP1 = p[1]
    p[1] = p[0]
    p[0] = oldP1 #update actual p in the argument
    return p


''' dictionaries can be mutated

pixel = {'r':50, 'g':100, 'b':200}
pixel['r'] = 20
pixel
{'r': 20, 'g': 100, 'b': 200}


keys in the dictionary have to be immutable data
strings are immutable

''' 

# ex of when you would want to use mutable dictionary
#tally (['pepsi','coke','coke','pepsi','coke']) should return {'pepsi':2, 'coke':3}

def tallyCokePepsi(votes):
    accum = {'pepsi':0, 'coke':0 }
    for vote in votes:
        if 'pepsi' == vote:
            accum['pepsi'] += 1
        else:
            accum['coke'] += 1
    return accum

def tallyCokePepsi2(votes):
    accum = {'pepsi':0, 'coke':0 }
    for vote in votes:
        accum[vote] += 1
    return accum

#more general

def tally(votes):
    accum = {}
    for vote in votes:
        if vote in accum:
            accum[vote] += 1 # accum[vote] = accum[vote] + 1 
        else:
            accum[vote] = 1  #adding to dictionary; cant use += because there is not value prior so only add one
    return accum
    

#memorization -- use a dictionary as a *memo table* to avoid recomputing things that we've already computed

def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def helperfib2(n,memotable): # <-- doesnt recompute
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memotable:
        return memotable[n]
    else:
        nthFib = helperfib2(n-1,memotable) + helperfib2(n-2,memotable)
        memotable[n] = nthFib
        return nthFib


def fib(n):
    return helperfib2(n,{})
























