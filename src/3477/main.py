from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()
        placed = set()
        for j, fruit in enumerate(fruits):
            print(f"Checking fruit {fruit}")
            for i, basket in enumerate(baskets):
                print(f"Checking basket {basket}, used are {used}")
                if i in used:
                    print(f"Basket {i} already used")
                    continue
                if basket >= fruit:
                    print(f"fruit {fruit} placed in {basket}")
                    used.add(i)
                    placed.add(j)
                    break
        
        return len(fruits) - len(placed)
        
if __name__ == "__main__":
    s = Solution()
    f = [3,10,10,2]
    b = [7,4,10,2]

    print(s.numOfUnplacedFruits(f, b))