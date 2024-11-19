import hw6

# as usual, add more tests here

def test_halveEvens():
    assert hw6.halveEvens([10,21,32,42,55]) == [5, 16, 21]
    assert hw6.halveEvens([]) == []
    assert hw6.halveEvens([13,35,47,55]) == []
    assert hw6.halveEvens([10,12,36,48,56]) == [5,6,18,24,28]
    

def test_splitEveryOther():
    assert hw6.splitEveryOther([1, 4, 23, 3, 8]) == [[1, 23, 8], [4, 3]]
    assert hw6.splitEveryOther([1, 3, 8]) == [[1,8],[3]]
    assert hw6.splitEveryOther([]) == [[],[]]
    assert hw6.splitEveryOther([1, 8]) == [[1],[8]]
    assert hw6.splitEveryOther([1]) == [[1],[]]


def test_isSorted():
    assert hw6.isSorted([1, 3, 3, 7]) == True
    assert hw6.isSorted([1, 3, 7, 3]) == False
    assert hw6.isSorted([1, 7, 3, 7]) == False
    assert hw6.isSorted([1, 7, 7, 7]) == True
    assert hw6.isSorted([]) == True
    

def test_dotProduct():
    assert hw6.dotProduct([1,2,3], [4,5,6]) == 32
    assert hw6.dotProduct([0], [0]) == 0
    assert hw6.dotProduct([2,3], [4,5]) == 23
    assert hw6.dotProduct([1], [4]) == 4
    assert hw6.dotProduct([],[]) == 0

    

example = [[{'r': 10, 'g': 23, 'b': 52}, {'r': 82, 'g': 3, 'b': 215}],
           [{'r': 30, 'g': 181, 'b': 101}, {'r': 33, 'g': 45, 'b': 205}]]

def test_negate():
    assert hw6.negate(example) == [[{'r': 245, 'g': 232, 'b': 203}, {'r': 173, 'g': 252, 'b': 40}],
                                   [{'r': 225, 'g': 74, 'b': 154}, {'r': 222, 'g': 210, 'b': 50}]]


def test_toDigitList():
    assert hw6.toDigitList(403) == [4, 0, 3]
    assert hw6.toDigitList(20) == [2,0]
    assert hw6.toDigitList(76858) == [7, 6, 8, 5, 8]
    assert hw6.toDigitList(7) == [7]
    
    

def test_digitalRootAndPersistence():
    assert hw6.digitalRootAndPersistence(9879) == {"root": 6, "persistence": 2}
    assert hw6.digitalRootAndPersistence(9) == {"root": 9, "persistence": 0}
    assert hw6.digitalRootAndPersistence(1000) == {"root": 1, "persistence": 1}
    assert hw6.digitalRootAndPersistence(8328932) == {"root": 8, "persistence": 2}
    
    
