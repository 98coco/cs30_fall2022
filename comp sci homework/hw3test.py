
import hw3

def test_remove():
    assert hw3.remove(4, [-2, 3, 4, 0, 4, 1]) == [-2, 3, 0, 1]
    assert hw3.remove(4, []) == []
    assert hw3.remove(6, [-2, 3, 4, 0, 4, 1]) == [-2, 3, 4, 0, 4, 1]
    assert hw3.remove(5, [5, 5, 5, 5, 5]) == []
    assert hw3.remove(6, [4,5,2,6,-3]) == [4, 5, 2, -3]


def test_countDistinct():
    assert hw3.countDistinct([5,3,2,2,5,1,3,2]) == 4
    assert hw3.countDistinct([6,5,2]) == 3
    assert hw3.countDistinct([0,0,0]) == 1
    assert hw3.countDistinct([]) == 0
    assert hw3.countDistinct([-6, 6, 7, 8, 2, 5, 6,]) == 6
     

def test_isSorted():
    assert hw3.isSorted([1, 2, 2, 8, 11]) == True
    assert hw3.isSorted([1, 2, 2, 1, 11]) == False
    assert hw3.isSorted([0, 0, 0, 0, 0]) == True
    assert hw3.isSorted([]) == True
    assert hw3.isSorted([-3, -6, 0, 8, 6]) == False

    
def test_insert():
    assert hw3.insert(4, [2,3,3,5]) == [2,3,3,4,5]
    assert hw3.insert(2, [2,3,3,5]) == [2,2,3,3,5]
    assert hw3.insert(0, [2,3,3,5]) == [0,2,3,3,5]
    assert hw3.insert(1, []) == [1]
    assert hw3.insert(0, []) == [0]

    
def test_merge():
    assert hw3.merge([1,3,5], [2,2,3,4]) == [1,2,2,3,3,4,5]
    assert hw3.merge([], [2,2,3,4]) == [2,2,3,4]
    assert hw3.merge([], []) == []
    assert hw3.merge([-1,3,5], [3,4]) == [-1, 3, 3, 4, 5]
    assert hw3.merge([2,2,3,4], []) == [2,2,3,4]


def test_mergeSort():
    assert hw3.mergeSort([1,5,3,2,2,1,3,2]) == [1,1,2,2,2,3,3,5]
    assert hw3.mergeSort([]) == []
    assert hw3.mergeSort([-3,-4,8,7,0]) == [-4,-3,0,7,8]
    assert hw3.mergeSort([7,8,5,2,3,5]) == [2,3,5,5,7,8]





















