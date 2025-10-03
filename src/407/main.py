from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        res = 0
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Get all the boundary cells
        pqueue = []
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(pqueue, (heightMap[i][j], i, j))
                    visited[i][j] = True

        while pqueue:
            ch, ci, cj = heapq.heappop(pqueue)
            for di, dj in DIRECTIONS:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    nh = heightMap[ni][nj]
                    if nh < ch:
                        res += ch - nh
                    heapq.heappush(pqueue, (max(nh, ch), ni, nj))
                    visited[ni][nj] = True

        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.trapRainWater(
            heightMap=[[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        )
    )
    print(
        s.trapRainWater(
            heightMap=[
                [3, 3, 3, 3, 3],
                [3, 2, 2, 2, 3],
                [3, 2, 1, 2, 3],
                [3, 2, 2, 2, 3],
                [3, 3, 3, 3, 3],
            ]
        )
    )
