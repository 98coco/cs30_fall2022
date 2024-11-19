import random

def magic8ball(question):
    options = ["definitely" , "No Way", "Maybe", "Try Again Tomorrow"]
    return random.choice(options)

# greet ('Coco') return 'Hi, Coco'

def greet(name):
    return "Hi " + name + "!"


#toPigLatin("python") returns "ythonpay"

def toPigLatin(word):
    #remove the first character, get remaining characters, add first letter after, and add ay
    first = word[0]
    middle = word[1:]
    return middle + first + 'ay'

#boolean values True and False

def test_toPigLatin():
    assert toPigLatin ('Todd') == "oddtay"
    assert toPigLatin ('potato') == "otatopay"
    assert toPigLatin ('Python')== "ythonpay"


