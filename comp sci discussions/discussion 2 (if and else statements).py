# IF Statments


if: expression1:
    statements(s)
elif:expression2:
     statements(s)
else:
     statements(s)

#Example
# Hamburger $10, Frieds 5, coffee 3, coke 1
# a guy goes to the store nd he wants to buy the most expensive thing


def buy(money):
    if money >= 10:
        return 'Hamburger'
    elif money >= 5:
        return 'fries'
    elif money >= 3:
        return 'coffee'
    elif money >= 1:
        'coke'
    else:
        return 'nothing'


#Recursive functions: functions that call themselves
# break up the problem into smaller pieces
#assume the function gives you the correct result
    #recursive cases - ccombine the result frm tail with head
    # base case - the simpllest case, when to stop

def length(l):  # [5,12,45,66]
    if l == []:
        return 0 # <- base case
    else:
        head = l[0] #5
        tail = l[1:] # [12,45,66] 
        recursiveResult = length(tail) #3
        return 1 + recursiveResult # <-- recursive case
