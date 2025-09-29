from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        minvol = len(grid) * len(grid[0])
        sp = self.splits(grid)

        for g1,g2 in sp:
            spg1 = self.splits(g1)
            for spg1g1, spg1g2 in spg1:
                vol = self.minimumArea(spg1g1) + self.minimumArea(spg1g2) + self.minimumArea(g2)
                minvol = min(minvol, vol)
            spg2 = self.splits(g2)
            for spg2g1, spg2g2 in spg2:
                vol = self.minimumArea(spg2g1) + self.minimumArea(spg2g2) + self.minimumArea(g1)
                minvol = min(minvol, vol)

        return minvol


    def splits(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        splits = []
        # Vertical splits
        last_found_zero = -1
        for col in range(cols - 1):
            # only if one of the elements is zero
            for row in range(rows):
                if grid[row][col] == 0:
                    last_found_zero = col
                    break
            
            if not (last_found_zero == col) and not (last_found_zero == col - 1):
                continue
            else:
                g1 = [x[:col + 1] for x in grid]
                g2 = [x[col + 1:] for x in grid]
                splits.append((g1, g2))
        
        # Horizontal splits
        last_found_zero = -1
        for row in range(rows - 1):
            # only if one of the elements is zero
            for col in range(cols):
                if grid[row][col] == 0:
                    last_found_zero = row
                    break
            
            if not (last_found_zero == row) and not (last_found_zero == row - 1):
                continue
            else:
                g1 = grid[:row+1]
                g2 = grid[row+1:]
                splits.append((g1, g2))
        return splits


    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        mini, minj = rows, cols
        maxi, maxj = 0, 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    mini = min(mini, i)
                    maxi = max(maxi, i)
                    minj = min(minj, j)
                    maxj = max(maxj, j)
        
        # print(maxj, minj, maxi, mini)
        return (maxj - minj + 1) * (maxi - mini + 1)

        
if __name__ == "__main__":
    s = Solution()
    inp = [[1,1],[0,1]]
    print(s.minimumSum(inp))