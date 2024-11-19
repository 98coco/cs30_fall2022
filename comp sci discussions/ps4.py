# 1. The function `removeOne(l, element)` takes two arguments: a list of integers `l` and the element to remove `element`
# It returns a list that is equal to `l` except that the first occurrence of the `element` is removed.
# If there are multiple occurrences of `element`, remove just the first one.
# If `element` is not present in the list `l`, return the original list `l`
# Example: removeOne([1,2,3], 2) == [1,3]
# Example: removeOne([1,2,3,2], 2) == [1,3,2]
# Example: removeOne([1,2,3], 10) == [1,2,3]


#type of input: list & integer
#type of output: list

def removeOne(l, element):
    if l == []:
        return []
    else:
        head = l[0] #1
        tail = l[1:] #2,3,2
        recursiveResult = removeOne(tail,element) #[1,3,2]
        if element == head:
            return tail
        else:
            return [head] + recursiveResult
    

# 2. The function `selectionSort(l)` returns the list `l` sorted from smallest to greatest.
# Your solution *must* make use of the `removeOne` function.  The idea of selection sort is as follows:  
# You can sort a non-empty list by removing the minimum element from the list (use the built-in min function to get the minimum element of a list) 
# and recursively sorting the rest of the list."
# Examples:
# selectionSort([1, 3, 5, -1, 0]) == [-1, 0, 1, 3, 5]
# selectionSort([1, 2, 3, 1, 3, 1]) == [1, 1, 1, 2, 3, 3] 

def selectionSort(l):
    if l == []:
        return []
    
    minimumElement = min(l)

    return [minimumElement] + selectionSort(removeOne(l,minimumElement))

# selectionSort is the recursion (rest of the list)



# 3. The function `getDigits(n)` returns a list of all the digits of `n`. 
# Assume that n > 0.
# Hint: Recall the flooring division function "//".
# Example: getDigits(123) ==[1, 2, 3]

#type of input = integer
# type of result = list

def getDigits(n):
    if (n < 10):
        return [n]
    else:
        digittoAdd = n%10 #3 modulus gives us remainder and remainder of thiss is the last digit of the number
        rest = n//10 #12
        recursiveResult = getDigits(rest) #[1,2]
        return recursiveresult + [digittoAdd]

'''

123 -->
        3(digittoadd)   12 (rest) -->
             2(digittoadd) ----> 1(rest)
                     1(digittoadd) ---> 0 (rest)

'''
        

# 4. The function `getNumber(l)` accepts a non-empty list of non-negative integers between 0 to 9 representing each digit of the original number n
# `getNumber(l)` should compute and return the original number. 
# Hint: this problem is easier if you focus on the last element of the list in each recursive call 
# Example: getNumber([1,2,3]) == 123

def getNumber(l):
    if len(l) == 1:
        return l[0]
    else:
        tail = l[len(l)-1] # last element of list
        head = l[0:len(l)-1] #everything but the last element of the list
        return getNumber(head)*10 + tail


# 5. The function `minPossibleNumber(n)` accepts a positive number n 
# it returns the minimum possible number you can get by rearranging the digits of `n`

# Hint: your solution can call all the functions we have covered in previous problems
# if there are 0s in the digits of the input number, they will be used as leading digits of the output number and can be ignored
# Examples:
# minPossibleNumber(2845) == 2458
# minPossibleNumber(31084) == 1348

#type of input: integers
#type of output: integers 

def minPossibleNumber(n):
    if 
    return n

'''
n = 241

a = get digits --> [2,4,1]
b = select sort --> [1,2,4]
c = get numbers --> 124

'''

# 6. (Challenge Question) Python lists can contain heterogeneous data. For instance, a list can contain sub-lists, like [1, [2, [3]]].
# Give a function `flatten(l)` that takes a heterogeneous list as an argument and returns a single list without any nested lists. 
# Note that the original ordering should be preserved.
# Examples:
# flatten([1, [1, [2, 3]]]) = [1, 1, 2, 3]
# flatten([[1, 2], [2, 4]]) = [1, 2, 2, 4]
# flatten([1,2,3,[4,5,6,[7,8,[9]]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
# flatten([]) = []
# 
# Hint: You can test if a variable `x` is a list by checking if its type is equal to `list`. For instance,
# if type(x) == list:
#   # x is a list!
# else:
#   # x is not a list.

def flatten(l):
    return l
