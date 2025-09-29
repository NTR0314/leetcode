from main import Solution

def test_1():
    nums = [6,4,3,2,7,6,2]
    expected = [12,7,6]
    
    calculated = Solution().replaceNonCoprimes(nums)

    assert calculated == expected, f"calculated {calculated}, expected {expected}"


if __name__ == "__main__":
    test_1()

