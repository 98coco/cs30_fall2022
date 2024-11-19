# a few problems will use functions from this library
import math

def totalSeconds(x,y,z):
    return x+(y*60)+(z*3600)

# write the function money

def money(x,y,z):
    return x * (1 + y/100) ** z

# write the function distanceFromNearestSquare

def distanceFromNearestSquare(x):
    # bottom square root of x
    lower = (math.isqrt(x)) ** 2
    higher = (math.isqrt(x)+1) ** 2
    return min(x - lower,higher - x)

# Have to put x before subtration for lower because x will always be bigger (comparing lowest) 
# Have to put x after subtraction for higher because x will always be smaller (comparing highest)
#positive numbers
    
# write the function isPrefix

def isPrefix(p,w):
    return w[0:min(len(p),len(w))] == p[0:min(len(p),len(w))]


# min gives numbers
# slicing gives text
#iif you index something with its own length you get it back


# write the function fromTotalSeconds

def fromTotalSeconds(x):
    hours = x//3600
    minutes = (x%3600)//60
    seconds = (x%3600)%60
    return [seconds,minutes,hours]
    
    
    
    
