from main import Solution

def test_1():
    n = 6
    delay = 2
    forget = 4
    expected = 5
    
    calculated = Solution().peopleAwareOfSecret(n, delay, forget)

    assert calculated == expected, f"calculated {calculated}, expected {expected}"

def test_2():
    n = 4
    delay = 1
    forget = 3
    expected = 6
    calculated = Solution().peopleAwareOfSecret(n, delay, forget)

    assert calculated == expected, f"calculated {calculated}, expected {expected}"

if __name__ == "__main__":
    test_1()
    test_2()