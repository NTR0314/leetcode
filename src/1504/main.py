from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # self.print_matrix(mat)
        rows = len(mat)
        cols = len(mat[0])

        lmat = [[0 for _ in range(cols)] for _ in range(rows)]
        res = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
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
                while ii >= 0 and mat[ii][j] == 1:
                    cur_max_left = min(cur_max_left, lmat[ii][j])
                    # print(f"i={i}, j={j}, ii={ii}, lmat[ii][j]={lmat[ii][j]}, res={res}")
                    res += cur_max_left
                    ii -= 1

        return res

    def print_matrix(self, mat):
        for row in mat:
            print(row)
        print()


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 1, 1, 1, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 0, 0]]
    assert (s.numSubmat(mat)) == 17
