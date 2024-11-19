#Floats = decimal numbers
# == to check if two variables are the same
# ==, <, >, <=, >= (conditional operators, return True or False)

#Strings (represent sequences of characters, specified w/ quotes, triple quotes for multiline
#Use three quotes for multi line strings
#Can acccess specified characters with [index] syntax
    #indexes start at 0; indexes end at one less than the number u called for (look at the example of 'abcdef'

    #x = 'abcde'
    #c = x[0]
    #d = x[4]

# concatenate  strings with +
    # x = 'abc' + 'def'
    
#can slice strings with [start:end] syntax
    # x = "abcdef'
    # y = x[1:4] "bcd" ; subtracting end and first gives you the length of the string
    # z = x[0:4] "abcd”

# comparing strings
    # conditional expressions
        # 'abc' == 'abcdef' #False
        # 'abc' > 'ab' #True
        # 'abcdef' < 'bc' #True (bc is greater because it starts at b; python is not going to look at the rest)

#list
    #represent sequences of items
        #can be multiplied different types
        #x = [“a”, “b”, “c”]
        #y = [“a”, 2, [1, 2, “c”], 4.0]
    #can concatenate list with +
    #can slice lists with [start:end]

# if statements only run code is the condition is true

#age = 5

#if age < 13:
    #print('you are not yet a teenager')
#difference between return & print =
    #print smth to a screen
    #return tells the computer you are done with a function and to bring it out to the outside function

#if statements
    #python requires a colon (:) after the condition and all the statements within the condition must be indented
    #Some other programming languages (C++) require the expression to be enclosed in parentheses, but that is optional in Python.
    #this also applies to elif statements

# input = input()
# number = int(input) --> int helps turn things into integers if it can

#if you have two or more if statements it will execute all the staatements
#elif helps you ignore he other if statements


#min function is a built in python function that returns the minimum of a number of values passed in as arguments
#for the min function you can psas list, or just values
#min can work for strings
#parameters are used for inputs

#a function does not need to return smth ; EX: printing 'hello world'
#for min we ask for it to return us smth so we can use the min for smth else 


# def is_product_less_than_equaal_100(x,y)
    #return x*z <= 100

# we dont have to use true or false for this function because less than
# and equal to or greater than aand equal to can be considered as booleans


#Syntax Error: The Python program is not 'grammatically' correct (ex: writing 'ded' instead of 'def'
#Name Error: You refer to an undefined variable
#Type Error: You are doing an operation with an invalid type (1 + 'test') (ex; subtracting a list from an integer)
#Indentation Error: You haven't correctly indented a line 


#What is recursion: a technique that solves problems by first solving
#smaller problems and using their solution to construct the final answer

#How does recursion work?
    #base case (since a recursive function calls itself, there must be a way to stop calling)
    #simplifying step (each time the recursive function is called, it must be called with a simpler
    #case of the problem to ensure tht we reach the base case

#fib(3) = 2
#fib (8) = 21

#type of n = integer
#type of result = integer

def fib(n):
    if n == []:
        return []
    elif n == 1:
        return 1   # you want two base cases because in the reccursive step it is asking to look at the two numbers before it;
                    #if you do not have 2 base cases it will try to call the second base and not be able to do anything
    else:
        return fib(n-1) + fib(n-2) # how the fiboncci numbers aare created

#type of l = list
#type of n = integer

def has_item(l,item):
    if []:
        return []
    else:
        head = [0] # 1 
        tail = [1:] #3,4,5
        recursiveResult = has_item(tail,item)
        if head == n:
            return True
        else:
            return false 


















    

    


