#boolean values True and False

# goal: write a function that takes a number and returns its absolute value

def test_absValue():
    assert absValue(3) == 3
    assert absValue(-5) == 5
    assert absValue(0) == 0

# test helps you with understanding the problem
    
def absValue(n):
    # n < 0 is the guard
    if n < 0:
        return n * -1
    else:
        return n

def test_toPigLatin():
    assert toPigLatin('hello') == 'ellohay'
    assert toPigLatin('python') == 'ythonpay'
    assert toPigLatin('iguana') == 'iguanaway'
    assert toPigLatin('apple') == 'appleway'

def toPigLatin(word):
    if startsWithAVowel(word):
        return toPigLatinVowel(word)
    else:
        return toPigLatinConsonant(word)

# startsWithAVowel('apple') should return True
# startsWithAVowel('hello') should return False

def startsWithAVowel(word):
    '''Returns a boolean indicating whetheer a given word starts with a vowel'''
    # docstring is what is listed above; when on playground, this docstring will explain what you are doing when you call a function
    first = word[0]
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        return True
    else:
        return False

def startsWithAVowel(word):
    first = word[0] 
    if first in ['a', 'e', 'i', 'o', 'u' ]:
        return true
    else:
        return False

def startsWithAVowel(word):
    first = word[0]
    return first in ['a', 'e', 'i', 'o', 'u']


def toPigLatinConsonant(word):
    first = word[0]
    rest = word[1:]
    return rest + first + 'ay'

def toPigLatinVowel(word):
    return word + 'way'


def intToSign(n):
    '''takes a number and returns either 'positive' or 'negative' or 'zero'. '''
    if n > 0:
        return 'positive'
    elif n < 0:
        return 'negative'
    else:
        return 'zero'

def intToSign4(n):
    if n == 0:
        answer = 'zero'
    elif n <0:
        answer = 'negative'
    else:
            answer = 'positive'
            return answer
    
def test_intToSign():
    assert intToSign(4) == 'positive'
    assert intToSign(-3) == 'negative'
    assert intToSign(-6) == 'negative'
    assert intToSign(0) == 'zero' 
    

