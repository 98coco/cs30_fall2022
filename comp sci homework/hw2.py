# used in the last part of the homework assignment
import turtle

def fizzBuzz(n):
    if n%15 == 0:
        return 'fizzbuzz'
    elif n%3 == 0:
        return 'fizz'
    elif n%5 == 0:
        return 'buzz'
    else:
        return n

def rps(player1,player2):
    if player1 == 'rock' and player2 == 'sissors':
        return 'player1 wins'
    elif player1 == 'rock' and player2 == 'paper':
        return 'player2 wins'
    elif player1 == 'scissors' and player2 == 'rock':
        return 'player2 wins'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'player1 wins'
    elif player1 == 'paper' and player2 == 'rock':
        return 'player1 wins'
    elif player1 == 'paper' and player2 == 'scissors':
        return 'player2 wins'
    else:
        return 'tie game'

    
def countPos(l):
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        recursiveResult = countPos(tail)
        if head > 0:
            return 1 + recursiveResult
        else:
            return recursiveResult

#type of l: list of integers
#type of n: integer
#type of result: list of integers
#adding 1 because we are looking for positive numbers and you start counting from 1 when there is a postive number

def threshold(l,n):
    if l == []:
        return []
    else:
        head = l[0] 
        tail = l[1:] 
        recursiveResult = threshold(tail,n) #need n to define what n is in the threshold
        if head <= n:
            return [n] + recursiveResult
        else:
            return [head] + recursiveResult

#adding head because it will only return part of the elements; you want to return all the elements including head


def intRange(low,high): 
    if low >= high: 
        return[]
    else:
        recursiveResult = intRange(low+1,high) 
        return [low] + recursiveResult
     

#type of l = list
#type of result = list
    
def innerLists(l):
    if l == []:
        return []
    else:
        head = l[0] #2
        tail = l[1:] #[5, 0, 1]
        recursiveResult = innerLists(tail) #[[1,2,3,4,5],[],[1]]
        if head == 0:
            return [[]] + recursiveResult
        else:
            return [intRange(1,head) + [head]] + recursiveResult


def regularNGon(n,sideLength):
    if n == 0:
        return
    else:
        drawNGon(n,360//n,sideLength)

# we use exterior angle bc it allows for the turtle to turn more

    
def drawNGon(n,angle,sideLength):
    if n == 0:
        return
    else:
        turtle.forward(sideLength)
        turtle.left(angle)
        recursiveResult = drawNGon(n-1,angle,sideLength)
        return
    

def archSpiral(length,increment,angle,n):
    if n == 0:
        return
    else:
        turtle.forward(length)
        turtle.left(angle)
        recursiveResult = archSpiral(length+increment,increment,angle,n-1)
        return 


#length+increment is tells us to move up/expand (we include increment to the length because length+increment is 
#how much we would move, increment tells us to maintain
#the increment throughout the whole drawing, angle tells us to maintain the angle
#throughout the whole drawing, and n-1 describes the rest of the sides needed


def logSpiral(length,percentIncrease,angle,n):
    if n == 0:
        return
    else:
        turtle.forward(length)
        turtle.left(angle)
        recursiveResult = logSpiral(length+(length*percentIncrease/100),percentIncrease,angle,n-1)
        return

# 100

# 4% increase --> 104










        
