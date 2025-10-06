from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        start = (0, 0)
        end = (len(grid) - 1, len(grid[0]) - 1)

        reached = set()
        unreached = []
        heapq.heappush(unreached, (grid[0][0], start))

        while unreached:
            cost, (x, y) = heapq.heappop(unreached)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(grid)
                    and 0 <= ny < len(grid[0])
                    and (grid[nx][ny], (nx, ny)) not in unreached
                    and (nx, ny) not in reached
                ):
                    reached.add((nx, ny))
                    heapq.heappush(unreached, (max(grid[nx][ny], cost), (nx, ny)))
                    if (nx, ny) == end:
                        return max(grid[nx][ny], cost)

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.swimInWater([[0, 2], [1, 3]]))
    print(
        s.swimInWater(
            grid=[
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
    )
