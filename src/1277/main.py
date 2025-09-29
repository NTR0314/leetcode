from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        lmat = [[0 for _ in range(cols)] for _ in range(rows)]
        res = 0

        # Create lmat
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    # lmat
                    if j > 0:
                        lmat[i][j] = lmat[i][j - 1] + 1
                    else:
                        lmat[i][j] = 1

        # self.print_matrix(lmat)
        for i in range(rows):
            for j in range(cols):
                ii = i
                cur_max_left = lmat[i][j]
                while ii >= 0 and matrix[ii][j] == 1 and cur_max_left >= (i - ii + 1):
                    if lmat[ii][j] < (i - ii + 1):
                        break
                    elif lmat[ii][j] < cur_max_left:
                        cur_max_left = lmat[ii][j]
                    # print(f"Found square: bottom-right=({i},{j}), size={i-ii+1}, res={res+1}")
                    res += 1
                    ii -= 1

        return res

    def print_matrix(self, mat):
        for row in mat:
            print(row)
        print()


if __name__ == "__main__":
    s = Solution()
    t1 = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
    assert s.countSquares(t1) == 15
    t2 = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
    assert s.countSquares(t2) == 7