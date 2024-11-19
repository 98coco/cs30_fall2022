import math

# Midterm Exam

#don't expect you to remember functions from math library

#you should know:
# len(length of a list of string)
# pow (exponentiation)
# min (get the minimum value in a list)
# slicing operation
# operators: +, -, / , // , *, %

#Language features:
# defining functions
# calling statements
# assignment statements
# return statements
# if/elif/else statements
# recursion (get recipe down)

#return the minimum element in a list of numbers
#l is a list of integers
#type of result: integer

def minimum(l): #[3,5,2,8,9]
        if l == []:
                return math.inf
        else:
                head = l[0]  #3
                tail = l[1:] #[5,2,8,9]
                recursiveResult = minimum(tail) # is an integer; can assume this will give us 2
                if head > recursiveResult:
                        return recursiveResult
                else:
                        return head

#different way to do minimum; this way is computing the minimum in parallel
                    
def min2(l): #([8,2,5,4,3,9,12,0])
    if l == []:
        return math.inf
    elif len(l) == 1:
        return l[0]
    else:
        mid = len(l)//2  #4 
        front = l[:mid] # remember slicing is exlusive at the last part so you wont get mid twice ; 8,2,5,4
        back = l[mid:] #slicing is inclusive of the first part; 3,9,12,0
        minFront = min2(front) #2
        minBack  = min2(back) #0
        if minFront < minBack:
            return minFront
        else:
            return minBack


#recursiveResult gives us the answer we want
#then we can use the head and the recursiveResult to see how they can work together to get an answer
#write down types


#brackets use for list



# example: fibonacci number
# 0,1,1,2,3,5,8,13.....

#fib(0) =0
#fib(1) = 1
#fib(n) = fib(n-1) + fib(n-2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#how many integers are anywhere in this list
# deepLen([5,32,[1,2,4], [[3],5], []] returns 7

def deepLen(l):
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        recursiveResult = deepLen(tail)
        if type(head) == list:
            return deepLen(head) + recursiveResult
#deepLen(head) is calling the function ex: deepLen([1,2,4])<-- this part solved in else; so 3 (3 integers in the list)+ recursiveResult
        else:
            return 1 + recursiveResult
    
































