import functools


# 1. doubleLargeStrings(l): given a list of strings, retain only the ones 
# that have length at least 5 and replace them with a list containing
# two copies of the string. 
# Example: ['hello','world','!'] --> [['hello','hello'],['world','world']]


def doubleLargeStrings(l):
    newList = list(filter(lambda x: True if len(x) >= 5 else False,l))
    return list(map(lambda x: [x] + [x],newList))

#brackets meaans adding the two words that are a list into the same list

# 2.1 Write a function noZeroLists that takes a list of lists and
# removes any inner lists that contain at least one 0 in them.

# Example: noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]])
# returns [[1,2,3], [], [1,1,1]].

# Hint: Python's "in" operator for checking whether a value is in a 
# list will be useful. 

def noZeroLists(l):
    return list(filter(lambda x: True if 0 not in x else False,l))

    return functools.reduce(lambda pr,curr: pr + [curr] if 0 not in curr else pr,l,[])


# 3. Write a function named count that takes an integer e and a list of integers l and 
# returns the number of occurrences of e in l.

# Note: please use only reduce to implement this function.
# ex: count(2, [1, 2, 2, 3, 2]) -> 3


def count(e,l):
    newList = functools.reduce(lambda pr,curr: pr + [curr] if e == curr else pr, l, [])
    return len(newList)
    
    newList = list(filter(lambda x: True if e == x else False,l))
    return len(newList)


# 4. Write a function innerMultiply that multiplies all elements of a 
# list of lists by a given number. For example, 
# innerMultiply([[1,2,3], [4,5]], 10) returns [[10,20,30], [40,50]].
# Hint: You'll need to use a map within a map!

def innerMultiply(l,n):
   return list(map(lambda x:list(map(lambda s: s*n,x)),l))

# ^^^ office hours ask why this works ; ask abt nesting 


# 5. Write a function named g that does the same thing the function h defined below.
# Example, h([1,3,6,5]) returns 13. Similarly, g([1,3,6,5]) returns 13


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

def g(l):
    return functools.reduce(lambda pr,curr: pr + [curr] if pr + [curr]%2 == 0 else pr, l, [])

#RECURSION

# 6. Write a function named pairify that concatenate each two elements in a 
# list to a new list.  
# Note: we assume the length of the list is always even.
# Example: pairify([1,5,6,8,9,10]) -> [[1,5], [6,8], [9,10]]

def pairify(l):
    if l == []:
        return []
    else:
        head1 = l[0]
        head2 = l[1]
        tail = l[2:]
        return [[head1] + [head2]] + pairify(tail)

# 7. Write a function named zip that takes two lists of the same length as 
# input,  and concatenate the elements from the same position of the two 
# lists to a new list. 
# Example1: zip1([1,2,3], [4,5,6]) -> [[1,4], [2,5], [3,6]]
# Example2: zip1([1], [4]) -> [[1, 4]]
# Example3: zip1([], []) -> []


def zip1(l1,l2):
    if l1 == [] and l2 == []:
        return []
    else:
        head1 = l1[0]
        head2 = l2[0]
        tail1 = l1[1:]
        tail2 = l2[1:]
        return [[head1]+ [head2]] + zip1(tail1,tail2)







