from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
        # Columns
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
                    
        # 3x3 Sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for ii in range(3):
                    for jj in range(3):
                        cell = board[i + ii][j + jj]
                        if cell != '.':
                            if cell in seen:
                                return False
                        seen.add(cell)
        
        return True
    

if __name__ == "__main__":
    inp = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    inp2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol = Solution()

    print(sol.isValidSudoku(inp))
    print(sol.isValidSudoku(inp2))
        