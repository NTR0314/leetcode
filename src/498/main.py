from enum import Enum
from typing import List

class Direction(Enum):
    TR = 1
    BL = -1

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i = 0
        j = 0

        result = []

        rows = len(mat)
        cols = len(mat[0])

        self.direction = Direction.TR

        changes = rows + cols - 1
        
        for lane in range(changes):
            diag_done = False
            while not diag_done:
                if self.direction == Direction.TR:
                    next_point = (i - 1, j + 1)
                else:
                    next_point = (i + 1, j - 1)
                    
                if next_point[0] < 0 or next_point[0] >= rows or next_point[1] < 0 or next_point[1] >= cols:
                    diag_done = True
                    if self.direction == Direction.TR:
                        self.direction = Direction.BL
                        # print(f"hit wall at {i}, {j}, adding {mat[i][j]}")
                        result.append(mat[i][j])
                        if j == cols - 1:
                            i += 1
                        else:
                            j += 1
                    else:
                        self.direction = Direction.TR
                        result.append(mat[i][j])
                        if i == rows - 1:
                            j += 1
                        else:
                            i += 1
                    continue
                
                result.append(mat[i][j])
                x, y = next_point
                i = x
                j = y


        return result        


if __name__ == "__main__":
    s = Solution()
    print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.findDiagonalOrder([[2,3]]))