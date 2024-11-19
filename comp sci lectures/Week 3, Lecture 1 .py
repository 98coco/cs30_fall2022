# in lets us know whether smth is in a list

#returns true if element e is in the list 1; otherwise it returns false
#example: contains (5, [1,2,3]) returns False
#type of e: integer
# Type of l : list of integers
#type of result: boolean (Trueor False)

def contains(e,l):
    if l == []:
        return False
    else:
        head = l[0]  #1
        tail = l[1:] #[2,3]
        recursiveResult = contains(e,tail) # what should contains (5, [2,3]) return? False
        return e == head or recursiveResult

#dupList([1,2,3]) == [1,1,2,2,3,3]

def dupList(l):
    if l == []:
        return []
    else:
        head = l[0] #1
        tail = l[1:] #2,3
        recursiveResult = dupList(tail) # [2,2,3,3]
        return [head, head] + recursiveResult

'''

#dupList([1,2,3])
l = [1,2,3]
head = 1
tail = [2,3]
    dupList ([2,3])
    l = [2,3]
    head = 2
    tail = 3
        dupList ([3])
        l = [3]
        head = 3
        tail = [] 
            duplist[] --> return[]
            recursiveResult = []
            return [3,3]
            RecursiveResult == [3,3]
            return [2,2,3,3]
        recursiveResults = [2,2,3,3]
        return [1,1,2,2,3,3]

'''

#given a list of strings, return a list containing only the words of length 4 or more
#example: longWords(['python','programming','is','super','fun'])

def longWords(l):
    if l == []:
        return []
    else:
        head = l[0] # python type: string
        tail = l[1:] #['programming', 'is', 'super', 'fun'] type: string
        recursiveResult = longWords(tail) # ['programming' and 'super']; list of strings
        if len(head) >= 4:
            return [head] + recursiveResult
        else:
            return recursiveResult

 # put brackets around head because recursiveResult is a list of strings
 # when adding things make sure they are of the same value; in this case ur adding a list w/ a list by adding the brackets around heaad
 # max on recursion means that your created a loop

'''Common Errors

ALWAYS: Look at the last red line and read it

* NameError: you are referring to a variable or function name that doesn't exist

*Type Error: You are passing the wrong type of aarguments to an operation
    (for example, trying to add an integer and a string)

*Recursion Error: your function runs forever. Check your reccursive call.
                Make sure that you recurse on the tail of the list.

* Type Error: longWords takes one positional argument but two were given.
    You are passing the wrong number or arguments to a function

*Index Error: Indexing into a list or string out of bounds
    examples: s = 'hello'
        s[17] causes and index error

*int is not subscriptable

You're using an int as if it's a string or list
    x= 3
    x[0]

'''

# recursion on numbers

# factorial

# factorial(n) = n * (n-1) *....*1

# factorial(n) = n * factorial(n-1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
