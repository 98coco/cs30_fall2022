def intToSign(n):
    if n>0:
        return 'positive'
    elif n<0:
        return 'negative'
    else:
        return '0'

# normal price of a ticket is $14
# senior price (65 and older) is $10
# non-senior and have a coupon, price is $12
#example: movieTickets (70,False) returns $10
# order of how if statements matter

# step 1: figure out what type of data is expeccte for each argument and what type of data
# is expected for the result
# age: integer (1,45,0...)
#coupon: boolean (True, False)
# result: integer
# step 2: write a test function with some asserts



def movieTickets(age,coupon):
    
    if age < 65 and coupon == True:
        return 12
    elif age < 65 and coupon == False:
        return 14
    else:
        return 10

def movieTickets2(age,coupon):
    if age < 65:
        if coupon:
            return 12
        else:
            return 14
    else:
        return 10

#can have if statements within other if statements
    
    
def test_movieTickets():
    assert movieTickets(70, False) == 10
    assert movieTickets(65, False)== 10
    assert movieTickets(80, True) == 12
    assert movieTickets(40, True) == 12
    assert movieTickets(30, False) == 14

def sumListExactly3(l):
    #assume the list has length exactly 3
    return 1[0]+l[1]+l[2]

# sumList[e1,e2,....,en] = e1+e2 + .... en

# interesting observation:
#sumList[e1,e2,....,en] can be defined in terms of
#  e1 and sumList[e2,....,en]

# sumList([e1,e2,....,en]) = e1 + sumList([e2,....,en])
# example: sumList([1,2,3]) = 1 + sumlist([2,3]) <-- we separated to show recurssion

# given a list [e1,e2,....,en]
# e1 is the *head* of the list
# [e2,...,en] is the *tail* of the list

# sumlist([]) = 0 

def sumList(l):
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        return head + sumList(tail)

'''
sumList ([1,2,3])
    return 1 + sumList([2,3])
                return 2 + sumList([3])
                        return 3 + sumList([])
                                    return 0
''' 
        
#recursion starts from the end 
#we took a number out of the list because it will allow us to reach 0
#by having a head and tail we can reach 0 and start computing from the end to give us an answer
#if we did not hav head or tail the function will keep going
#for recursions we have to break things down in order to get back to the top; if we did not it will keep going


'''
Recipe for recursion on lists:

def f(l)
    if l == []:
    # this is called the base case
    # usually easy
    <insert code here>
    else:
        #this is called the recursive case
        head = l[0]
        tail = l[1:]
        recursiveResult = f(tail)
        <combine head and recursiveresult in some way to get desired answer>
        
''' 

def length(l):  # [5,12,45,66]
    if l == []:
        return 0
    else:
        head = l[0] #5
        tail = l[1:] # [12,45,66] 
        recursiveResult = length(tail) #3 <- this will give us 3
        return 1 + recursiveResult

    # 1 is counting head as 1 number

# incrementList([1, 4, 7]) = [2,5,8]

def incrementList(l):
    if l == []:
        return []
    else:
        head = l[0] #1
        tail = l[1:] #4,7
        recursiveResult = incrementList(tail) #[5, 8]
        return [1+ head] + recursiveResult #have to do in this order or you will reverse the list
    # adding one because increments are adding by 1

# can assume that the reccursiveResult already gave you the tail
# how does python know how to add 1 to every number

'''
incrementList([1,4,7])
    return [1+1] + incrementList([4,7])
                    return [1+4] + incrementList ([7])
                                    return [1+7] + incrementList([])
                                                        return []                                 
'''

# sum only the positive elements of a list
# sumPositives ([1,2,-4,5,0])=8
# type of l" list of integers
# type of result: integers
def sumPositives(l):
    if l == []:
        return 0
    else:
        head = l[0] #1
        tail = l[1:] #[2,-4,5,0] 
        recursiveResult = sumPositives(tail) #7
        if head > 0:
            return head + recursiveResult
        else: head < 0:
            return recursiveResult
        
    
# head + recursiveResult beacause it will add all the elements; we only want positive

# dupList ([1, 2, 3]) = [1, 1, 2, 2, 3, 3]
 # def dupList(l):
