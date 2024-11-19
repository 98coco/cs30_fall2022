# Practice problems for loops

import functools

# example: firstPositive([0, -4, -2,5, 1, 0]) == 5

def firstPositiveLoop(l):
    '''Returns the first positive number in l, or -1 if there is none.'''
    for i in range(len(l)):
        if l[i] > 0:
            return l[i]
        else:
            l[i+1]
    return -1


def firstPostiveFilter(l):
    posList = list(filter(lambda x: x > 0, l))
    return posList[0] if len(posList) > 0 else -1
    
#return postive list then 1 pos


def firstPositiveRecursion(l):
    if l == []:
        return -1
    else:
        head = l[0]
        tail = l[1:]
        if head > 0:
            return head
        else:
            return firstPositiveRecursion(tail)
            


# example: indexOfFirstPositive([0, -4, -2, 5, 1, 0]) == 3
def indexOfFirstPositive(l):
    '''Returns the index of the first positive number in l, or -1 if there is none.'''
    for i in range(len(l)-1):
        if l[i] > 0:
            return i
        else:
            l[i+1]
    return -1


# example: sumConsecutive([1, 4, 3, 7]) = [5, 10]
def sumConsecutive(l):
    '''Returns a list resulting from summing consecutive elements of l.
You may assume that the list has an even number of elements.'''
    accum = []
    for i in range(len(l))[::2]:
        accum += [l[i] + l[i+1]]
    return accum


# example: commonPrefix('python', 'pylon') == 'py'

def commonPrefix(s1, s2):
    '''Returns a string that is the maximal prefix shared by strings s1 and s2.
The two strings need not have the same length.'''
    accum = ''
    minLen = min(len(s1),len(s2))
    for i in range(minLen):
        if s1[i] == s2[i]:
            accum += s1[i]
        else:
            accum
    return accum


# example: hasTwoInARow([2, 1, 2, 3, 3, 1]) == True
def hasTwoInARow(l):
    '''Returns True if l has two of the same element in a row and False otherwise.'''
    res = False
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return True
        else:
            res
    return res


# example: hasTwoOfTheSame([4, 1, 2, 3, 1, 0]) == True
def hasTwoOfTheSame(l):
    '''Returns True if l has two of the same element and False otherwise.'''
    res = False
    accum = []
    for i in range(len(l)):
        if l[i] in accum:
            return True
        else:
            accum += [l[i]]
    return res

    




















