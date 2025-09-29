from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]

        if numRows <= 2:
            if numRows == 1:
                return [[1]]
            else:
                return res

        for i in range(2, numRows):
            row = res[-1]
            tmp_res = [1]
            for i in range(len(row) - 1):
                tmp_res.append(row[i] + row[i+1])
            tmp_res.append(1)
            res.append(tmp_res)

        return res
        
if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))