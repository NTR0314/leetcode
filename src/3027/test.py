from main import Solution

def test_1():
    print("Test 1")
    points = [[3,1],[1,3],[1,1]]
    expected = 2
    assert Solution().numberOfPairs(points) == expected
    
def test_2():
    points = [[1,1],[2,2],[3,3]]
    expected = 0
    assert Solution().numberOfPairs(points) == expected

def test_3():
    points = [[6,2],[4,4],[2,6]]
    expected = 2

    assert Solution().numberOfPairs(points) == expected

def test_4():
    points = [[2,5],[128653,-2370425]]
    expected = 1

    assert Solution().numberOfPairs(points) == expected
    
def test_5():
    points = [[2,6],[2,4]]
    expected = 1
    

    assert Solution().numberOfPairs(points) == expected

if __name__ == "__main__":
    test_5()
    test_4()
    test_3()
    test_2()
    test_1()
    print("All tests passed.")