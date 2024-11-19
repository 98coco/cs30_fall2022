import functools

### Section1. use map/filter/reduce to solve the 1-5 questions. ###


# 1. doubleLargeStrings(l): given a list of strings, retain only the ones 
# that have length at least 5 and replace them with a list containing
# two copies of the string. 
# Example: ['hello','world','!'] --> [['hello','hello'],['world','world']]

def doubleLargeStrings(l):
    newList = functools.reduce(lambda partialResult,currElem: partialResult + [currElem] if len(currElem) >= 5 else partialResult, l, [])
    return functools.reduce(lambda partialResult,currElem: partialResult + [[currElem,currElem]], newList,[])

    return list(map(lambda x: [x]+[x], list(filter(lambda x: len(x) >=5,l))))


# 2.1 Write a function noZeroLists that takes a list of lists and
# removes any inner lists that contain at least one 0 in them.
# Example: noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]])
# returns [[1,2,3], [], [1,1,1]].
# Hint: Python's "in" operator for checking whether a value is in a 
# list will be useful. 

#use filter to take out list w 0

def noZeroLists(l):
    return list(filter(lambda x: True if 0 not in x else False,l))
    

# 2.2 Implement the noZeroLists function again only with reduce.
def noZeroLists_2(l):
    return functools.reduce(lambda pr,curr: pr if 0 in curr else pr + [curr], l, [])

#[curr after pr bc u add from front to back) 
#type of result is a list of list 

# 3. Write a function named count that takes an integer e and a list of integers l and 
# returns the number of occurrences of e in l.
# Note: please use only reduce to implement this function.
# ex: count(2, [1, 2, 2, 3, 2]) -> 3

def count(e, l):
    newList = functools.reduce(lambda pr,curr: pr + [curr] if curr == e else pr, l, [])   
    return len(newList)


def countFor(e,l):
    accum = 0
    for x in l:
        if x == e:
            accum += 1
        else:
            accum
    return accum

#[curr] will give us what we want ex:[1,2,3] and not [curr] becaause it is
#just a varible in a list; it is not defining a value

# 4. Write a function innerMultiply that multiplies all elements of a 
# list of lists by a given number. For example, 
# innerMultiply([[1,2,3], [4,5]], 10) returns [[10,20,30], [40,50]].
# Hint: You'll need to use a map within a map!

#type of input == list of list and integer 
#type of output == list of list 

def innerMultiply(l, n):
    return list(map(lambda x:list(map(lambda y: y * n,x)),l))


# function list(map(lambda y: y * n,x)) is multplying each element in the list
# x is seen as the list  --> outer of the map is return list of list 


# 5. Write a function named g that does the same thing the function h defined below.
# Example, h([1,3,6,5]) returns 13. Similarly, g([1,3,6,5]) returns 13

def h(l):
    return helper(l, 0)

'''

1  
    3  
         6   
             5   
                

 0 (presum) + 1 (head) = 1
 1 (presum) - 3 (head)  = 2
 2 (presum) + 6(head) = 8
 8 (presum) + 5(head) = 13


'''

# returning value at bottom --> returning the last value to each step (before it change previous returns because we were affecting the tail from the outside

def h(l):
    return helper(l, 0)

def helper(l, preSum):
    if l == []:
        return preSum
    else:
        head = l[0] #1 
        tail = l[1:] #3,6,5
        if preSum % 2 == 0:  #if presum is even 
            return helper(tail, preSum + head)
        else:
            return helper(tail, preSum + 1)

#base on this information use reduce because you are adding elements 

def g(l):
   return functools.reduce(lambda pr,x: pr + x if pr%2 == 0 else pr + 1,l,0)


### Section2. use recursive functions to solve the following problems. ###


# 6. Write a function named pairify that concatenate each two elements in a 
# list to a new list.  
# Note: we assume the length of the list is always even.
# Example: pairify([1,5,6,8,9,10]) -> [[1,5], [6,8], [9,10]] 

def pairify(l):
    if l == []:
        return []
    else:
        head1 = l[0] #1
        head2 = l[1] #5
        tail = l[2:] #6,8,9,10
        return [[head1] + [head2]]+ pairify(tail)
        
        


# 7. Write a function named zip that takes two lists of the same length as 
# input,  and concatenate the elements from the same position of the two 
# lists to a new list. 
# Example1: zip1([1,2,3], [4,5,6]) -> [[1,4], [2,5], [3,6]]
# Example2: zip1([1], [4]) -> [[1, 4]]
# Example3: zip1([], []) -> []

def zip1(l1, l2):
    if l1 == [] and l2 == []:
        return []
    else:
        head1 = l1[0]
        head2 = l2[0]
        tail1 = l1[1:]
        tail2 = l2[1:]
        return [[head1] + [head2]] + zip1(tail1,tail2)
        


# 8.*(challenge)* Implement unzip(l) function which is the inverse of zip. 
# Note: we assume every list in l contains two elements. 
# Example: unzip([[1,4], [2,5], [3,6]]) -> [[1,2,3], [4,5,6]]

# unzip ([[1,4]]) --> [1],[4]

def unzip(l):
    if l == []:
        return [[],[]]
    else: # l = [[3, 6]]
        head = l[0] # [3, 6]
        tail = l[1:] # []
       # unzip(tail) = [[3], [6]]
        return [[head[0]] + unzip(tail)[0]] + [[head[1]] + unzip(tail)[1]]
        # return [[3] + unzip(tail)[0]] + [[6]+unzip(tail)[1]]
        # unzip(tail)    [0] = unzip([])[0] = unzip([]) = []
        # unzip([]) -> []
        # unzip([[3, 6]]) -> [[3],[6]]
        


   # + [head[1]] + unzip(tail)

#start from bottom up

'''

[1,4] ---> [1,2,3] , [4,5,6]
    [2,5] --> [2,3],[5,6]
        [3,6] -->  [3],[6]
             []

''' 
    

# 9. *(challenge)* A *sublist* of a list l is a list one can form by removing
# zero or more elements from l: for instance, [1, 3] is a sublist of [1,2,3,4],
# since one can remove 2 and 4 from [1, 2, 3, 4] to form [1, 3]. By definition,
# both [] and l itself are always sublists of any list l.
# Implement allsublists(l) which, given a list l, returns
# list of all sublists one can form from l. The returned list can be in any order: all
# that matters is that it contains each sublist exactly once.
# Example: allsublists([1, 2, 3]) == [[], [1], [2], [3], [1,2], [1,3], [2, 3], [1, 2, 3]]
#          allsublists([1,1]) == [[], [1], [1], [1,1]]
# Hint: if l = [1,2,3], in the first iteration, head = 1, recursiveResult is [[], [2], [3], [2,3]]
#       final result is [[], [2], [3], [2,3]] + [[1], [1,2], [1,3], [1,2,3]]
def allsublists(l):
    return l


#Return the sum of the numbers in the array, returning 0 for an empty array
#Except the number 13 is very unlucky so do not count 13

def sum13(l):
  return functools.reduce(lambda pr,curr: pr + curr if curr != 13 else pr,l,0)



def rightTriangles(l):
    return list(filter(lambda x: True if x[0]**2 + x[1]**2 == x[2]**2 else False,l))



def threshold(l,n):
    return list(map(lambda x: x if x>n else n,l))



def countOccurrences(f,l):
    newList = list(filter(f,l))
    return len(newList)


# rightTriangles([[2, 3, 4], [3, 4, 5], [5, 12, 13], [8, 10, 12]])
#type of input - list of lsit
#type of output - list of list 


def rightTriangles2(l):
    if l == []:
        return []
    else:
        head = l[0] #[2,3,4]
        tail = l[1:] #[[3, 4, 5], [5, 12, 13], [8, 10, 12]]
        if head[0]**2 + head[1]**2 == head[2]**2:
            return [head] + rightTriangles2(tail)
        else:
            return rightTriangles2(tail)


def toUpper(s):
    if ord(s) >= 97 and ord(s) <= 122:
        return chr(ord(s)-32)
    else:
        return s

def toLower(s):
    if ord(s)>= 65 and ord(s)<=90:
        return chr(ord(s)+32)
    else:
        return s

def allLower(s):
    newList = list(map(lambda x: toLower(x),s))
    return functools.reduce(lambda pr,curr: pr + curr,newList,'')



def capitalize(s):
    newList = list(map(toLower,s))
    cap = toUpper(newList[0])
    cor = [cap] + newList[1:]
    return functools.reduce(lambda pr,curr: pr + curr,cor,'')


#ofh question: does it add '' first  <- yes names curr ad a value


def title(s):
    lower = list(map(allLower,s))
    capital = list(map(lambda x: capitalize(x) if len(x) >= 4 else x,lower))
    return [capitalize(lower[0])] + capital[1:]


def count_evens(l):
    newList = list(filter(lambda x: True if x%2 == 0 else False,l))
    return len(newList)

    
    
def big_diff(l):
    maxi = functools.reduce(lambda pr,curr: curr if curr > pr else pr, l)
    mini = functools.reduce(lambda pr,curr: curr if curr < pr else pr, l)
    return maxi - mini


# cant use filter because filter to get max and min cause filter will return
# a list and u can't subtract list from list


#do not count numbers 6 

def sum67(l):
    return functools.reduce(lambda pr,curr: pr if curr == 6 else curr + pr,l,0)


# do not count numbers 6 & 7

def sum671(l):
    return functools.reduce(lambda pr,curr: pr + curr if curr != 6 and curr != 7 else pr,l,0)











