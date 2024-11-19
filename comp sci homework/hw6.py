
# Read the homework description carefully!


def halveEvens(l):
    res = []
    for x in l:
        if x%2 == 0:
            res += [x//2]
        else:
            res 
    return res


# if index is even put in one list, if index is odd put in another lsit

def splitEveryOther(l):
    accum = []
    accum2 = []  #accumulators have to be outside so that once the loop ends the values can just go in those list
    for i in range(len(l)):
        if i%2 == 0:
            accum += [l[i]]
        else:
            accum2 += [l[i]]
    return [accum, accum2]


# compare the next element


def isSorted(l):
    res = True
    for i in range(len(l)-1): #indexes
        if l[i] > l[i+1]:
            return False
        else:
            res = True
    return res


def dotProduct(a1,b1):
    res = 0
    for i in range(len(a1)): #it is ok to just do the index of one list bc both are the same length 
        res += a1[i] * b1[i]
    return res



def negate(l):
    res = []
    for x in l: # all pixels
        accum = []
        for y in x: #one row/list
            accum += [{'r':255 - y['r'], 'g': 255 - y['g'], 'b':255 - y['b']}]
        res += [accum] 
    return res



def toDigitList(n):
    res = []
    while n != 0:
        res += [n%10]
        newN = n//10
        n = newN
    return res[::-1]

        

def digitalRootAndPersistence(n):
    res = {'root':0, 'persistence':0}
    p = 0 #how many times while loop has gone
    while n > 10:                   #cause u stop adding stuff once there is a single digit
       getR = sum(toDigitList(n))    #9+8+7+9 = 33
       n = getR  #newN until it is a single digit
       p += 1    #everytime while loop has run add 1
    r = n
    res = {'root': r, 'persistence':p}
    return res













        
