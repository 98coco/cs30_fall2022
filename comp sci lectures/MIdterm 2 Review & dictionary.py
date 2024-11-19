    
import functools

# midterm review
#   reduce w/ and w/o a lambda
#   multiple recursive calls
#   map within map
#   order of operations in recursion, map, filter, reduce
#   recursion w/ helper
#   paassing functions on functions
#   arguments to lambda


def sumList(l): #[1,2,3]
    if l == []:
        return 0
    else:
        head = l[0] #1
        tail = l[1:] #2,3 
        recursiveResult = sumList(tail) #5 
        return head + recursiveResult

# (1 + (2 +(3+0)))
# forwrd to unroll the recursive call and then computes backwards // reduce does this forwards


def sumList2(l):
#                                   3   3                    
    return functools.reduce(lambda pr,curr: pr + curr, l, 0)

# (((0+1) + 2) + 3)
# every call to plus is the call to lambda
#think of it as partial result as the result except for the last elem; last elem can be see as curr elem
# how do we incorporate curr eelem to partial result to get what we want

def add(x,y):
    return x + y

def sumList(l):
    return functools.reduce(add,l,0)

# ^^^ w/o lambda
# dont need lambdas u can call another function


# functools.reduce(x,y: x-y, [1,2,3],0) <-- start w/ base and first part of the list
# (((0-1) -2) -3) == -6 


#true if there are only positives in l; otherwise return false

def allPositives(l):
    return functools.reduce(lambda pr,curr: False if curr <= 0 else pr ,l,True)
                            
  #  return list(filter(lambda x: True if x > 0 else False))


def allPositives2(l):
    return functools.reduce(lambda pr, curr: currelem > 0 and pr,l,True)

#pr is a boolean 



def double(n):
    return n *2


def twice(f,n):
    return f(f(n))

# example: twice(double,4) = 16
# has to be a function w/ one argument for twice
#f == function
#n == integer


#increment inner list ([[1,2,3],[],[3,4,5]]) = [[2,3,4],[],[4,5,6]]
#1. increment the values in a list of numbers
#2. use that to increment all list in a list of list of numbers 



#([1,2,3]) = [2,3,4]
#takes a list of numbers and returns a list of numbers
def incrementList(l):
    return list(map(lambda n: n + 1,l))

#write aa function that solves the inner list (incrementList) then write a function for the bigger list 

#incrementInnerList ([[1,2,3],[],[3,4,5]]) = [[2,3,4],[],[4,5,6]]

#takes a list of lsit of numbers and returns aa list of list of numbers

def incrementInnerList(l):
    return list(map(incrementList,l))

#passing function to map; map calls on increment list when applying to L


def incrementInnerList(l):
    return list(map(lambda innerL:list(map(lambda n: n + 1,innerL)),l))
    

#study
# what is computed first & last
# writing lambda & reduce (try practicing boolean problemms too)
# base cases (ex: mergeSort on hw)



#--------------


#library for rational numbers (fraction)

# ['num': 1, 'denom':3] <-- have to build rational numbers and this is our representation

import math



def lowestTerms(r):
    num = r ["num"]
    denom = r["denom"]
    g = math.gcd(num,denom)
    return {"num": num//g, "denom": denom//g}

#a/b * c/d  = ac/bd

def multiplyRationals(r1,r2):
    num1 = r1['num']
    denom1 = r1['denom']
    num2 = r2['num']
    denom2 = r2['denom']
    return lowestTerms({'num': num1 * num2, 'denom': denom1 * denom2})
    
# multiplyRationals({"num": 1, "denom":3},{"num": 1, 'denom':3})

def printRational(r):
    print(str(r['num'])+str(r['denom']))




# --------- TEST HOMEWORKS ------------


def remove(l,n):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        if n == head:
            return remove(tail,n)
        else:
            return [head] + remove(tail,n)


def countDistinct(l):
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        return 1 + countDistinct(remove(l,head))
    

def merge(l1,l2):
    if l1 == [] and l2 == []:
        return []
    elif l1 != [] and l2 == []:
        return l1
    elif l1 == [] and l2 != []:
        return l2
    else:
        head1 = l1[0]
        head2 = l2[0]
        tail1 = l1[1:]
        tail2 = l2[1:]
        if head1 > head2:
            return [head2] + merge(l1,tail2)
        elif head1 < head2:
            return [head1] + merge(tail1,l2)
        else:
            return [head1] + [head2] + merge(tail1,tail2)























