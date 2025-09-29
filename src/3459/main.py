from functools import cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dirs = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, direction, turn, target) -> int:
            nx, ny = i + dirs[direction][0], j + dirs[direction][1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != target:
                return 0
            tmp = dfs(nx, ny, direction, turn, 2 - target)
            
            if turn:
                nd = (direction + 1) % 4
                tmp = max(tmp, dfs(nx, ny, nd, False, 2 - target))
                
            # print(f"dfs({i}, {j}, {direction}, {turn}, {target}) = {tmp + 1}")

            return tmp + 1
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        res = max(res, dfs(i, j, direction, True, 2) + 1)

        return res
        
    
# --- IGNORE ---

if __name__ == "__main__":
    s = Solution()
    inp = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    print(s.lenOfVDiagonal(inp))