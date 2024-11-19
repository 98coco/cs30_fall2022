

#type of input: integer and list
#type of output: list 

def remove(n,l):
    if l == []:
        return []
    else:
        head = l[0] #-2
        tail = l[1:] #3,4,0,4,1
        recursiveResult = remove(n,tail) #3,0,1
        if n == head:
            return recursiveResult
        if n > head or n < head:
            return [head] + recursiveResult


#type of input: list
#type of output: integer
        
def countDistinct(l):
    if l == []:
        return 0
    else:
        head = l[0] #5 
        tail = l[1:] #3,2,2,5,1,3,2
        recursiveResult = countDistinct(tail) #3 <-- only counting tail
        return 1 + countDistinct(remove(head,l) )

    #thinking: everytime you remove head - you add 1 

#type of input: list
#type of output: boolean T or F

def isSorted(l):
    if l == []:
        return True
    else:
        head = l[0] #1
        tail = l[1:] # 2,2,8,11
        recursiveResult = isSorted(tail) #True
        if head <= min(l):
            return recursiveResult 
        else:
            return False


#compare head w/ another element
#going thru each element to see if it is sorted least to greatest
#if head <= min (l) it checks the rest of recursiveResult which is the tail of the list

def insert(n,l):
    if l == []:
        return [n]
    else:
        head = l[0] #2
        tail = l[1:] #3,3,5
        recursiveResult = insert(n,tail) #2,3,3,4,5  (insert n,l <- l is not being reduced) 
        if n <= head:
            return [n] + l #dont need recursive after adding it to the list so just return the rest of the list  
        else:
            return [head] + recursiveResult 

#type of input: list
#type of output: list

def merge(l1,l2):
    if l1 == [] and l2 == []:
        return []
    elif l1 == [] and l2 != []:
        return l2
    elif l1 != [] and l2 == []:
        return l1
    else:
        head1 = l1[0] # 1
        tail1 = l1[1:] #3,5
        head2 = l2[0] #2
        tail2 = l2[1:] #2, 3, 4
        recursiveResult = merge(tail1, tail2) #[1] + 2,2,3,3,4,5
        if head1 < head2: #least to greatest
            return [head1] + merge(tail1,l2)
        elif head1 == head2:
            return [head1] + [head2] + recursiveResult
        else:
            return [head2] + merge(l1,tail2)

#type of input: list
#type of output: list
        
def mergeSort(l):
    if len(l) <= 1:
        return l
    else:
        mid = len(l)//2
        list1 = l[0:mid]
        list2 = l[mid:]  
        return merge(mergeSort(list1),mergeSort(list2))
    
        
       






