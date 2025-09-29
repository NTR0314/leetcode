from main import Solution

def test_1():
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    expected = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
    
    calculated = Solution().spellchecker(wordlist, queries)

    assert calculated == expected, f"calculated {calculated}, expected {expected}"

def test_3():
    wordlist = ["YellOw"]
    queries = ["yollow"]
    expected = ["YellOw"]

    calculated = Solution().spellchecker(wordlist, queries)

    assert calculated == expected, f"calculated {calculated}, expected {expected}"

def test_2():
    wordlist = ["v","t","k","g","n","k","u","h","m","p"]
    queries = ["n","g","k","q","m","h","x","t","p","p"]
    expected = ["n","g","k","","m","h","","t","p","p"]

    calculated = Solution().spellchecker(wordlist, queries)

    assert calculated == expected, f"calculated {calculated}, expected {expected}"

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
