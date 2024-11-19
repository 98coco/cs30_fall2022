# Midterm:
#closed book/notes/computer
#just pencil and paper
#short answer & multiple choice & programming problems
#cover everything up to October 12 (no picobot or turtle)
#discussion section this friday will be midterm praactice
#monday review


#variations on standard recursion recipe

#one situation: need multiple base cases, or different base case

#another situation: recurse on something other than the tail of the list


#return a new list every consecutive pair of numbers is added
#addConsecutive([1,5,3,8]) returns [6,11]
#addConsecutive([1,5,3]) returns [6,3]
#addConsecutive([5]) returns [5]
#type of l is a list of integers
#type of result is a list of integers

def addConsecutive(l):
    if l == []: #base case for even
        return []
    elif len(l) == 1: #for an odd list (this helps w/ the last number) <-- base case for odd
        return l #l is alr a list of integer so we can write l 
    else:
        first = l[0] #1
        second = l[1] #5
        rest = l[2:] #3,8
        recursiveResult = addConsecutive(rest) #[11] <- this is  a list 
        return [first + second] + recursiveResult #brackets around first and second because those are integers


#keep every other element of the list
#example: everyother([1,4,7,10,5]) return [1,7,5]
#type of l is a list of integers
#type of result is a list of integers
    
def everyOther(l):
    if l == []:
        return []
    else:
        first = l[0] #1
        allButFirstTwo = l[2:] #7
        recursiveResult = everyOther(allButFirstTwo)
        return [first] + recursiveResult
    


#returns True ifs1 is a prefix of s2 

def isPrefix(s1,s2): # 'hole','hello'
    if s1 == '':
        return True #empty string is a prefix of any other string
    elif s2 == '':
        return False # if s1 is not empty and s2 is then it automatically returns false
    else:
        head1 = s1[0] #'h'
        tail1 = s1[1:] #'ole'
        head2 = s2[0]  #'h'
        tail2 = s2[1:] #'ello'
        if head1 == head2:
            return isPrefix(tail1,tail2) #checking the rest of the word to see if they match <-- this is our recursive case
        else:
                return False

def isPrefixEitherDirection(s1,s2):
    if s1 == '' or s2 == '':
        return True 
    else:
        head1 = s1[0] #'h'
        tail1 = s1[1:] #'ole'
        head2 = s2[0]  #'h'
        tail2 = s2[1:] #'ello'
        if head1 == head2:
            return isPrefix(tail1,tail2) #checking the rest of the word to see if they match <-- this is our recursive case
        else:
                return False

#zip([1,2,3],[4,5,6]) returns [[1,4],[2,5],[3,6]]
#assume that the lists have the same length
#type of l1 is a list of integeers
#type of l2 is a list of integers
#type of result is a list of list of integers

def zip(l1,l2):
    if l1 == []: # dont need to add l2 because we assume that both are the same length
        return []
    else:
        head1 = l1[0] #1
        tail1 = l1[1:] #2,3
        head2 = l2[0] #4 
        tail2 = l2[1:] #5,6
        recursiveResult = zip(tail1,tail2) #2,3 and #5,6
        return [[head1] + [head2]] + recursiveResult # head 1 is a list and head 2 is a list; we need to put the two heads and turn it into a list of list


#takes a non-empty list of strings and returns True if the very first string is longer
#than every other string in the list, otherwise returns False

#firstIsLongest(['programming','is','fun']) returns True
#firstIsLongest(['is', 'programming','fun']) returns False
# if we use one recursive result then we will lose the first element


def firstIsLongest(l):
    head = l[0]
    tail = l[1:]
    return stringisLongerThanAll(tail,head)



#define a more general function
#takes  list of strings l and a string s and returns True if s is longer
#than every string in l, otherwise returns False
# l list a list of strings
#s is string
#result is a boolean

def stringisLongerThanAll(l,s):
    if l == []:
        return True
    else:
        head = l[0]
        tail = l[1:]
        if len(head) > len(s):
            return False
        else:
            return stringisLongerThanAll(tail,s)
    
    


#if you need extra variable, create another general function and then call
#that function in the one you need





    
