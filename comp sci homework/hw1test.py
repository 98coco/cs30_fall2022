
import hw1

# add more tests to each of these functions!
# and make sure to run each of them!

def test_totalSeconds():
    assert hw1.totalSeconds(3, 2, 1) == 3723
    assert hw1.totalSeconds(0, 0, 0) == 0
    assert hw1.totalSeconds(4,3,1) == 3784
    assert hw1.totalSeconds(7,6,4) == 14767
    assert hw1.totalSeconds(5,7,8) == 29225

def test_money():
    assert hw1.money(100, 20, 2) == 144.0
    assert round(hw1.money(400,30,3),4) == 878.8
    assert round(hw1.money(200,20,3),1) == 345.6
    assert round(hw1.money(100,30,5),3) == 371.293
    assert round(hw1.money(150,25,2),3) == 234.375
    assert round(hw1.money(200,25,8),8) == 1192.09289551
    
# as long as you use up to rounding 4 decimal places your test should be good

def test_distanceFromNearestSquare():
    assert hw1.distanceFromNearestSquare(13) == 3
    assert hw1.distanceFromNearestSquare(15) == 1
    assert hw1.distanceFromNearestSquare(23) == 2
    assert hw1.distanceFromNearestSquare(38) == 2
    assert hw1.distanceFromNearestSquare(50) == 1

def test_isPrefix():
    assert hw1.isPrefix('hel', 'hello') == True
    assert hw1.isPrefix('h','hello') == True
    assert hw1.isPrefix('uc','ucla') == True
    assert hw1.isPrefix('ucla','uc') == True
    assert hw1.isPrefix('understand','under') == True
    assert hw1.isPrefix('happy','sad') == False
    

def test_fromTotalSeconds():
    assert hw1.fromTotalSeconds(3723) == [3, 2, 1]
    assert hw1.fromTotalSeconds(4000) == [40,6,1]
    assert hw1.fromTotalSeconds(8000) == [20,13,2]
    assert hw1.fromTotalSeconds(8943) == [3, 29,2]
