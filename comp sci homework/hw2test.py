
import hw2

# add more tests to each of these functions!
# and make sure to run each of them!

def test_fizzBuzz():
    assert hw2.fizzBuzz(1) == 1
    assert hw2.fizzBuzz(3) == 'fizz'
    assert hw2.fizzBuzz(25) == 'buzz'
    assert hw2.fizzBuzz(15) == 'fizzbuzz'
    assert hw2.fizzBuzz(28) == 28
    assert hw2.fizzBuzz(30) == 'fizzbuzz'

def test_rps():
    assert hw2.rps('rock', 'paper') == 'player2 wins'
    assert hw2.rps('paper','rock') == 'player1 wins'
    assert hw2.rps('scissors','rock') == 'player2 wins'
    assert hw2.rps('scissors','scissors') == 'tie game'
    assert hw2.rps('scissors','paper') == 'player1 wins'


def test_countPos():
    assert hw2.countPos([1, -4, 0, 4, 8, 0]) == 3
    assert hw2.countPos([3, -2, -1, 8, 9, 7]) == 4
    assert hw2.countPos([-5, -4, -6, -7, -2, -1]) == 0
    assert hw2.countPos([0, 0, 0, 0, 0, 0]) == 0
     

def test_threshold():
    assert hw2.threshold([1, -4, 0, 4, 8], 1) == [1, 1, 1, 4, 8]
    assert hw2.threshold([3, 9, 7, 1, -8], 5) == [5, 9, 7, 5, 5]
    assert hw2.threshold([0, 0, 0, 0, 0], 2) == [2, 2, 2, 2, 2]
    assert hw2.threshold([4, 12, 5, 8, 5], 3) == [4, 12, 5, 8, 5]


def test_intRange():
    assert hw2.intRange(2, 5) == [2, 3, 4]
    assert hw2.intRange(5,4) == []
    assert hw2.intRange(6,9) == [6,7,8]
    assert hw2.intRange(0,0) == []
    assert hw2.intRange(3,2) == []
    assert hw2.intRange(2,3) == [2]
    assert hw2.intRange(2,2) == []
                        


def test_innerLists():
    assert hw2.innerLists([2, 5, 0, 1]) == [[1,2], [1,2,3,4,5], [], [1]]
    assert hw2.innerLists([0, 0, 0, 0]) == [[], [], [], []]
    assert hw2.innerLists([1, 5, 6, 1]) == [[1],[1,2,3,4,5],[1,2,3,4,5,6],[1]]

# testing your turtle drawings is a bit more complicated, since those functions
# don't return any results.  in the tests below we simply run the functions
# so you can look at the output.  you should add more tests. but in class on Monday
# October 10 we will see how you can, and should, do a better job of testing these
# functions than simply running them.

def test_regularNGon():
    hw2.regularNGon(8, 100)


def test_archSpiral():
    hw2.archSpiral(1, 0.5, 30, 100)


def test_logSpiral():
    hw2.logSpiral(1, 4, 30, 120)
