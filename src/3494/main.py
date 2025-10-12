from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        if not skill or not mana:
            return 0

        # init
        n = len(skill)
        dp = [0] * n
        dp[0] = skill[0] * mana[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + skill[i] * mana[0]
            
        print(dp)

        for j in range(1, len(mana)):
            cur_potion = mana[j]
            
            dp[0] += skill[0] * cur_potion
            
            for i in range(1, n):
                brewing_time = skill[i] * cur_potion
                dp[i] = max(dp[i], dp[i-1]) + brewing_time
            
            for j in range(n-2,-1,-1):
                dp[j] = dp[j+1] - skill[j+1] * cur_potion

            print(dp)
        
        return dp[-1]
        

        
    def minTime2(self, skill: List[int], mana: List[int]) -> int:
        
        cur = [0] * len(skill)
        for i, wiz in enumerate(skill):
            cur[i] = wiz * mana[0] + cur[i - 1] if i > 0 else wiz * mana[0]
            
        # print(f"{cur=}")
        for potion in mana[1:]:
            if not len(skill) == 1:
                for i in range(len(skill) - 1, -1, -1):
                    cur_wiz_brewing_time = skill[i] * potion
                    # print(f"\n{cur_wiz_brewing_time=}, {i=}")
                    if i == len(skill) - 1:
                        cur[i] += cur_wiz_brewing_time
                        # print(f"incremented cur[{i}] = {cur[i]}")
                    else:
                        next_wiz_brewing_time = skill[i + 1] * potion
                        cur[i] = max(
                            cur[i + 1] - next_wiz_brewing_time,
                            cur[i] + cur_wiz_brewing_time,
                        )
                        # print(f"cur[{i}] = {cur[i]}, down: {cur[i]=}+{cur_wiz_brewing_time=}, " +
                            # f"right: {cur[i+1]=}+{next_wiz_brewing_time=}")
                # Forward pass from first wiz to last wiz
                for i in range(1, len(skill)):
                    cur[i] = cur[i - 1] + skill[i] * potion
                # print(f"{cur=}")
            else:
                cur[0] = cur[0] + skill[0] * potion

            
        return cur[-1]

    
if __name__ == "__main__":
    s = Solution()
    print(s.minTime([1, 5, 2, 4], mana = [5, 1, 4, 2]))
    print(s.minTime(skill=[5], mana = [8, 3]))
        