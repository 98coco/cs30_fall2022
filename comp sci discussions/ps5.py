from functools import reduce
# Map, Filter, Reduce (use reduce when we have 2 arguments)

#1. minutesToSeconds(l): convert a list of minutes into a list of seconds.

def minutesToSeconds(l):
    return list(map(lambda n: n*60,l)) 

#2. Fahren2Cels(l): given a list of temperatures in fahrenheit, 
# convert them to celsius, round the result to the nearest integer and return
# Hint: fahrenheit to celsius formula is to subtract by 32 then multiply by 5/9
# round() will round to the nearest integer
# for example Fahren2Cels([72,32,0]) --> [22, 0, -18]

def Fahren2Cels(l): 
    return  list(map(lambda n: (n-32)*5//9,l))


#3. punctuation(l): given a list of strings, remove all strings that end 
# in '?' but add '!' to the end of all other strings.
# e.g. ['hello?', 'world'] --> ['world!']

def punctuation(l):
    newList = list(filter(lambda s: True if s[len(s)-1] != '?' else False,l))
    return list(map(lambda s: s + '!',newList)) 


#4. Write a function average(l) that takes a non-empty list of numbers
# and returns their average.
# Note: avoid using sum() function. 

def average(l):
    return reduce(lambda x,y: x+y, l, 0)/len(l)


#5. Professor Pennypincher enjoys a 10% educational discount on anything he buys. 
# However, he will not buy anything if he has to pay strictly more than 200 dollars after the educational discount. 
# Write a function pennypincher 
# that takes a list of prices and returns the total amount that Professor 
# Pennypincher would have to pay, if he bought everything that was cheap 
# enough for him. For example, pennypincher([100, 150, 200, 210, 250]) 
# returns 594.0.

#filter then map

def pennypincher(l):
    discountedPrice = list(map(lambda n: n - (n * 10/100),l))
    newList = list(filter(lambda x: x <= 200, discountedPrice))
    return reduce(lambda x,y: x+y, newList,0)


#6. Professor Puzzler is a crossword enthusiast. She has a long list of
# words that might appear in a crossword puzzle, but she has trouble 
# finding the ones that fit a slot. Write a function crosswordFind to 
# help her. The expression crosswordFind(letter, inPosition, length, words)
# should return all the items from the list words which 
#(1) are of the given length and 
#(2) have letter in the position inPosition.
# For example, if Puzzler is looking for seven-letter words that have 'k' 
# in position 1, he can evaluate the expression:  
# crosswordFind('k', 1, 7, ["funky", "fabulous", "kite", "icky", "ukelele"]) 
# which returns ["ukelele"].

def crosswordFind(letter, position, length, wordList):
    words = list(filter(lambda n: len(n) == length,l))
    return list(filter(lambda n: n[pos] == letter, words))


#first step: filter by len
#second step: filter based on position














