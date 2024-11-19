
import hw4

def test_rightTriangles():
    assert hw4.rightTriangles([[2, 3, 4], [3, 4, 5], [5, 12, 13], [8, 10, 12]]) == [[3, 4, 5], [5, 12, 13]]
    assert hw4.rightTriangles([]) == []
    assert hw4.rightTriangles([[2, 3, 4],[8,10,12]]) == []
    assert hw4.rightTriangles([[3, 4, 5], [5, 12, 13]]) == [[3, 4, 5], [5, 12, 13]]
    assert hw4.rightTriangles([[3, 4, 5], [5, 12, 13]]) == [[3, 4, 5], [5, 12, 13]]
    


def test_threshold():
    assert hw4.threshold([1, -4, 0, 4, 8], 1) == [1, 1, 1, 4, 8]
    assert hw4.threshold([1, -4, 0, 4, 8], 1) == [1, 1, 1, 4, 8]
    assert hw4.threshold([3, 9, 7, 1, -8], 5) == [5, 9, 7, 5, 5]
    assert hw4.threshold([0, 0, 0, 0, 0], 2) == [2, 2, 2, 2, 2]
    assert hw4.threshold([], 3) == []


def test_countOccurrences():
    assert hw4.countOccurrences(lambda x: x > 0, [1, -4, 0, 4, 8, 0]) == 3
    assert hw4.countOccurrences(lambda x: x < 0, [1, -4, 0, 4, 8, 0]) == 1
    assert hw4.countOccurrences(lambda x: x%2 != 0, [2, 4, 6]) == 0
    assert hw4.countOccurrences(lambda x: x%2 == 0, [2, 4, 6]) == 3
    


def test_toUpper():
    assert hw4.toUpper('b') == 'B'
    assert hw4.toUpper('B') == 'B'
    assert hw4.toUpper('A') == 'A'
    assert hw4.toUpper('a') == 'A'
    assert hw4.toUpper('C') == 'C'
    assert hw4.toUpper('c') == 'C'
    assert hw4.toUpper('T') == 'T'
    assert hw4.toUpper('t') == 'T'


def test_toLower():
    assert hw4.toLower('b') == 'b'
    assert hw4.toLower('B') == 'b'
    assert hw4.toLower('A') == 'a'
    assert hw4.toLower('a') == 'a'
    assert hw4.toLower('C') == 'c'
    assert hw4.toLower('c') == 'c'
    assert hw4.toLower('T') == 't'
    assert hw4.toLower('t') == 't'

def test_allLower():
    assert hw4.allLower('hElLO') == 'hello'
    assert hw4.allLower('') == ''
    assert hw4.allLower('hello') == 'hello'
    assert hw4.allLower('HELLO') == 'hello'
    assert hw4.allLower('Hello') == 'hello'
    assert hw4.allLower('And') == 'and'
    assert hw4.allLower('Zebra') == 'zebra'


def test_capitalize():
    assert hw4.capitalize('hElLO') == 'Hello'
    assert hw4.capitalize('string') == 'String'
    assert hw4.capitalize('HELLO') == 'Hello'
    assert hw4.capitalize('Rain') == 'Rain'
    assert hw4.capitalize('TraIn') == 'Train'


def test_title():
    assert hw4.title(['pRIde', 'AND', 'PREJUDICE']) == ['Pride', 'and', 'Prejudice']
    assert hw4.title(['tHe', 'souND', 'AND', 'the', 'fUrY']) == ['The', 'Sound', 'and', 'the', 'Fury']
    assert hw4.title(['MIDNIGHTS','BY','TAYLOR', 'SWIFT']) == ['Midnights','by', 'Taylor','Swift']






