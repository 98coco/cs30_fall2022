# Final Exam
# Friday December 9, 8-11am
#cumulative
# same format as the midterms

# new topics since the last midterm:
# - dictionaries
# - for loops (by element, by index)
# - while loops
# -  mutations

#common prefix problem
#while loops
#nested loops
#mutations
#recursion
#tally

# for loops are best for list because you are walking over smth; walking once per element of a list; also walk over strings
# while loop is good for when you dont know how many times to go over smth

# while condition: (operates like a condition - true or false) 
#   statements
#difference - use while loop when trying to meet a condition

# as long as condition evaluates to True, execute statements -- when conditions are false exit the loop
# and go to the next line

#one difference between for loop and while loop:
#   for loop terminates bc it is going over a list that ends
#   while loops have the possibly of the terminating

# to terminate while loops change the value of ur argument


#return the longest common prefix
#commonPrefix("hey","hello") returns "he"


#first: let's assume that s1 and s2 have the same length
#   walk over the strings to see where they are equal
#   want to walk over s1 AND s2 at the same time
#   loop over indexes

def commonPrefixForSameLength(s1,s2):
    accum = ''
    for i in list(range(len(s1))):
        if s1[i] == s2[i]:
            accum += s1[i]
        else:               # need else to stop the accum or else the loop will keep going and add common strings to the accum 
            return accum
    return accum
    


def commonPrefixWhileSameLength(s1,s2): #have to do it manually bc while loops work manually
    accum = ''
    i = 0
    while i < len(s1): 
        if s1[i] == s2[i]:
            accum += s1[i]
        else:              
            return accum
        i += 1
    return accum


#s1 and s2 different lengths

def commonPrefixFor(s1,s2):
    accum = ''
    minlen = min(len(s1), len(s2))
    for i in list(range(minlen)):
        if s1[i] == s2[i]:
            accum += s1[i]
        else:               # need else to stop the accum or else the loop will keep going and add common strings to the accum 
            return accum
    return accum


def commonPrefix(s1,s2): #have to do it manually bc while loops work manually
    accum = ''
    i = 0
    while i < min(len(s1), len(s2)):
        if s1[i] == s2[i]:
            accum += s1[i]
        else:              
            return accum
        i += 1
    return accum


#sumConsecutive([1,4,7,3]) = [5,10]

def sumConsecutiveWhile(l):
    accum = []
    i = 0
    while i < len(l):
        accum += [l[i] + l[i+1]]
        i += 2  #skip two because u alr handled two
    return accum
        

def sumConsecutiveFor(l):
    accum = []
    for i in list(range(len(l)))[::2]:
        accum += [l[i] + l[i+1]]
    return accum


#natural place for nested loops (list within list)

#sumListOfList([[2,4],[3],[6,7,4]]) = 26

def sumListOfList(l):
    s = 0
    for innerL in l:  # list inside the whiole list ; executes 3 times for the example above
        for x in innerL: #executes 6 times for example above  -- dont need accumulator here bc adding is associative but u can hav an accumulator
            s += x
    return s

def sumListOfList(l):
    s = 0
    for innerL in l:  # list inside the whiole list ; executes 3 times for the example above
        innerS = 0
        for x in innerL: #executes 6 times for example above  
            innerS += x
        s += innerS
    return s
            
#can also call function / break problem into two pieces; equivalent without nested loops:

def sumList(l):
    res = 0
    for x in l:
        res += x
    return res

def sumListOfList2(l):
    s = 0
    for innerL in l:
        s += sumList(innerL)
    return s 


#Understand mutation

#rule 1: variables always hold references (like an address) to data, rather than the data itself
#rule 2: copying a variable always copies the reference, not the data

#mypair = [10,20]
#incPair(mypair)

def incPair(p): # p is [10,20]
    first = p[0]  # first is [10]
    first = first +1  #first is [11]             
    p[1] = p[1] +1 #p[1] is 21 -- in place update of p[1] so it updated for mypair as well
                    #mypair is now [10,21] (10 stays the same bc we did not do an inplace update) 
    return [first, p[1]] #[11,21]



# p[1] = p[1] +1 (nonlocal update)
# if we did second = p[1] and second = p[1] +1 this will not change mypair
# first = first +1 (local update -- only updating the variable first not p[0]) 


#tally(['c', 'p', 'p'] = {'c':1, 'p':2}

#need mutation bc as u go u want to update the tallies 

def tally(l):
    d = {}
    for vote in l:
        if vote in d: # is vote already a key in the dictionary
            d[vote] += 1  
        else:
            d[vote] = 1  #not in dictionary then add it to dictionary 
    return d
            



#recursion
#"self similarity" property: you can solve a problem by first solving a smaller
#version of that same problem
#solve a problem for a list l by first solving the problem for the tail l

#base case: how to solve the smallest problem (for a lsit, when the list is empty)
#recursive case: solve the problem for l by first solving the problem for its tail

#sumList([x1, ..., xn])

def sumListRecurs(l):
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[:1]
        return head + sumListRecurs(tail) #sumList is the rest of the list -- magic of recursion assume this gives u wat u want

#think abt recursive -- what do i want to do w the head w the previosu result


















    








