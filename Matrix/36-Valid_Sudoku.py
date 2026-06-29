# Problem Link:https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150

# method 1: hash set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # check each row
        cols = [set() for _ in range(9)]  # check each column
        squares = [set() for _ in range(9)]  # check each 3x3 square

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                squ_index = (i // 3) * 3 + j // 3

                if num in rows[i] or num in cols[j] or num in squares[squ_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                squares[squ_index].add(num)

        return True

# T: (9^2)
# S: O(9^2)