
#2nd Midterm 
# in class next Wednesday (Nov 9) --> similar format as the 1st midterm

#Topics (everythings covered by hw3 and hw4):
#   fancier recursion (e.g. multiple recursive calls)
#   map/filter/reduce
#   lambda
#   passing functions to other functions/retaining functions as results


#print displays information

# typing hello returns 'hello' on the playground
# print('hello') returns hello without quotes on the playground


#difference between print and return:
#ex:
#   double(34) + 10 returns 78
#   badDouble(34) + 10 displays 68 and a type error of 'unsupported operand type(s) for 'Nonetype' and 'int)


def double(n):
    return 2 * n

    #return computes the information and displays the final result

def badDouble(n):
    print (2 * n)

    # ur not getting anything back from it  --> print does uses data by shpwing data; it does not give daata
    #print just DISPLAYS DATA

import random

def magic8Ball(question):
    return random.choice(
        ['Definitely!','Maybe','Not a Chance','Ask again tomorrow!'])


def magicApp():  #an APP does not take any arguments ; just gets data from user and displays that data to the user
    #input a question from the user
    question = input('Give me a yes/no question:')  #input is a blocking function // block smth until it gets called 
    answer = magic8Ball(question)
    print ('The answer is:' + answer)


#PYTHON DICTIONARY ----

# student = ['Josie Bruin', 1038932, 100, 75, 100] 
#   if we do this it will require us to index and sometimes it is hard to tell what each part of the list represents


#dictionary allows us to label data -- associating a key to a value
#EX: student = {'name': 'Josie Bruin' , 'id': 1038932, 'midterm1': 100, 'hw1': 75, 'hw1':100}
#   student['name'] returns 'Josie Bruin'

#can make a list of dictionaries for all students
# EX: [{'name': 'Josie Bruin' , 'id': 1038932, 'midterm1': 100, 'hw1': 75, 'hw1':100}, {'name': 'Joe Bruin' , 'id': 105899, 'midterm1': 100, 'hw1': 86 'hw1':90}]
#   downside of list is that you need to know the index of the list 

# {} = swirly brackets make it a dictionary
# : = assigns the key to a value 

#dictionary would represent one student
#list of dictionary would represent same data for different students 

#-----------

#Dictionary Practice Problems

#midterm is worth 50%
#homework is worth 25%
#example: computeFinalGrade({'name': 'Josie Bruin' , 'id': 1038932, 'midterm1': 100, 'hw1': 75, 'hw2': 90})

#in dictionary u want to give names to each piece of data; you can use different types of data ffor dictionary
#we still need to include '' in strings when making a key for dictionary because it is still a piece of python data

def computeFinalGrade(student):
    return student['midterm1'] * 0.5 + student['hw1'] *.25 + student['hw2'] * .25    

import functools 


#type of student: list of dictionaries
    
def averageMidtermScores(students):
    #type of partialResult : number
    #type of currElem : dictionary - each students is represented as a dictionary 
    sumOfMidterm = functools.reduce(lambda partialResult, student: partialResult + student['midterm1'], students,0)
    return sumOfMidterm // len(students)
    
# students = [{'name': 'Josie Bruin' , 'id': 1038932, 'midterm1': 100, 'hw1': 75, 'hw1':100},
#  {'name': 'Joe Bruin' , 'id': 105899, 'midterm1': 100, 'hw1': 86 'hw1':90}]

def name(students):
    return list(map(lambda students: {students['name']},students))

def averageMidtermScores2(students):
    #type of student: list of dictionaries
    listofMidtermScores = list(map(lambda student: student['midterm1'], students))  #only gives us the list of midterm scores; #dont use filter bc it will take out midterm1
    return sum(listofMidtermScores) // len(listofMidtermScores)


#type of student: list of dictionaries

def highestFinalGrade(students):
    eachFinalGrade = list(map(computeFinalGrade,students))
    return max(eachFinalGrade)

def highestFinalGrade2(students):
    return functools.reduce(lambda partialResult,student: partialResult if partialResult > computeFinalGrade(student) else computeFinalGrade(student), -1)











