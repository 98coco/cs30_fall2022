import functools

# Write your functions here!

def rightTriangles(l):
    return list(filter(lambda x: False if x[0]**2 + x[1]**2 != x[2]**2 else True,l))
    
#right triangle a^2 + b^2 = c^2
#filter
# x[0] = a, x[1] = b, x[2] = c


def threshold(l,n):
    return list(map(lambda x: n if x < n else x,l))

#map to compare every number in the list
#if statements 


def countOccurrences(f,l):
    newList = list(filter(f,l))
    return len(newList)
    
#filter out the ones that do not apply to the function
#apply the function on the list
#add one for every number the function is true

def toUpper(s):
    if ord(s) >= 97 and ord(s) <= 122: #lowercase 
        return chr(ord(s)-32) #uppercase subtract by 32 bc the diff between lower and upper is 32
    else:
        return s
    

def toLower(s):
   if ord(s) >= 65 and ord(s) <= 90: # uppercase
       return chr(ord(s)+32)
   else:
        return s

def allLower(s):
    newList = list(map(toLower,s))
    return functools.reduce(lambda partialResult,currElem: partialResult + currElem, newList, '')

#use map to lowercase each element
#use reduce to add the strings together 


def capitalize(s):
    lowerCase = list(map(toLower,s))
    upperCase = toUpper(lowerCase[0])
    newList = [upperCase] + lowerCase[1:]
    return functools.reduce(lambda partialResult,currElem: partialResult + currElem, newList, '') 


#lowercase everything
#index the first part of the list
#capitalize the first part of the list
#add everything together 


def title(s):
    lower = list(map(allLower,s)) #lowercase the whole list
    upperCase = list(map(lambda x: capitalize(x) if len(x) >= 4 else x,lower))
    return [capitalize(s[0])] + upperCase[1:]

    
#check the length of each element in the list
#capitalize the strings w/ len greater than 4 

#title(['tHe', 'souND', 'AND', 'the', 'fUrY'])

