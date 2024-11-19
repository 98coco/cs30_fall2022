

# x += y is the same as x = x + y


def doubleAll(l):
    res = []
    for x in l:
        res = res + [2 * x]
    return res


def reverse(l):
    res = []
    for x in l:
        res = [x] + res
    return res


#looping over indexes

#indexValuePairs([4,6,-9)] = [[0,4] , [1,6], [2,-9]]

def indexValuePairs(l):
    res = []
    i = 0
    for x in l:
        res += [[i,x]]
        i += 1
    return res

def indexValuePairs2(l):
    res = []
    for i in range(len(l)):
        res += [[i,l[i]]]  # l[i] is the value in the index
    return res

# sumAll([[1,3], [2,4,6], [], [5]]) = 21 -- explaining nested loop

def sumAll(l):
    res = 0
    for innerL in l:
        res += sum(innerL)
    return res


def sumAll2(l):
    res = 0
    for innerL in l: # out for loop (first value of innerL is [1,3]
        for x in innerL: # goes into the [1,3] and add it then goes back to the outside and moves onto the next element [2,4,6]
            res += x
    return res

'''
[1,3]
1
3
[2,4,6]
2
4
6
[]
[5]
5
return 21

'''


#squareAll([[1,3], [2,4,6], [], [5]]) = [[1,9],[4,16,36], [], [25]]

def squareAll(l):
    res = [] #list for outside
    for innerL in l:
        accum = [] #need one here to bc we are creating list w the values inside
        for x in innerL:
            accum += [x ** 2]
        res += [accum]  # adding what we got from the innerlist to the final solution
    return res 


 #square all elements in a list of numbers

def squareList(l):
    res = []
    for x in l:
        res += [x*x]
    return res


# squre all elements in a list of lsit

def squareAll2(l):
    res = []
    for innerL in l:
        res += [squareList(innerL)]
    return res 




# for loops are a form of *bounded loop* -- they execute for a known number of times
#(once per element of the list) and then are done

#sometimes you dont know in advance how many times you want to execute a loop

#need an unbounded loop

#example: Euclid's algorithm for computing greatest common divisor


#gcd(m,0) = m
#gcd(m,n) = gcd(n,m%n)

#gcd(20,12)= gcd(12,8) = gcd(8,4) = gcd(4,0) = 4
#gcd(20,13) = gcd(13,7) = gcd(7,6) = gcd(6,1) = gcd(1,0) = 1
#gcd (20,15) = gcd(15,5) = gcd(5,0) = 5

# ^^ example above demonstrates how you dont know how many times you want to execute a loop


def gcdRecursive(m,n):
    if n == 0:
        return m
    else:
        return gcdRecursive(n, m%n)

# WHILE LOOP -- write this w/ while loop

# while e:  # while e is true keep doing the statements in the next line until false
#   statements


# keep executing statements over and over while e evaluates to True

#once you have a while loop you do not need a for loop bc a while loop can perform everything a for loop can
#when going over a list use for loop bc it will be easier


#usually use while loop for a boolean

'''

while x < 10:
    print(x)
    x = x+1

will give u -

0
1
2
3
4
5
6
7
8
9

while True:
    print('hi')  < -- will go on forever 

'''


# using while loop for GCD

def gcdWrong(m,n):
    while n!= 0:
        m = n # m = 12
        n = m % n # n = 12 so 12%12 = 0; needs to  evaaluate the old value of m too 
    return m 

# ^^ this equation is wrong

def gcd(m,n):
    while n!= 0:
        origM = m
        m = n  # m = 12
        n = origM % n # 0 
    return m 


def sqaureListWhileLoop(l):
    i = 0
    res = []
    while i < len(l): # still in the bounds of the list 
        res += [l[i] * l[i]]
        i += 1
    return res

# sqaureListWhileLoop([1,2,3,4]) = [1,4,9,16]

# Collatz conjecture (3n +1 probllem)
#start with a number n
#If it's even then halve them
#otherwise then multiple it by 3 and add 1

# question: if you keep doing this, you will reach 1

#13, 40, 20, 10, 5, 16, 8, 4 , 2, 1
#14,7,22,11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4 ,2, 1

def collatz(n):
    while n!= 1:
        if n%2 == 0:
            n == n//2
        else:
            n = 3 * n + 1
    return n 

def collatz2(n):
    c = 0
    while n!= 1:
        c += 1
        if n%2 == 0:
            n == n//2
        else:
            n = 3 * n + 1
    return c 

def collatz3(n):  #allows u to see the numbers 
    accum  = []
    while n!= 1:
        accum += [n]
        if n%2 == 0:
            n == n//2
        else:
            n = 3 * n + 1
    accum += [n]
    return accum


import random

#example: number guessing game

def guessingGame():
   secret = random.randint(1,100)

   sGuess = input("Guess a number between 1 and 100:")
   guess = int(sGuess)

   while guess != secret:
       if guess > secret:
           sGuess = input("Lower!")
       else:
            sGuess = input("Higher!")
       guess = int(sGuess)
            
   print("You Win Slay!")


def guessingGame2():
   secret = random.randint(1,100)

   sGuess = input("Guess a number between 1 and 100:")
   guess = int(sGuess)

   while guess != secret:
       if guess > secret:
           sGuess = input("Lower!")
       else:
            sGuess = input("Higher!")
       guess = int(sGuess)
       
       print("You Win Slay!")
       again = input("Do you want to play again?")
       if again == "yes":
           guessingGame()
       else:
           print ("Thanks for playing!")


       









    
