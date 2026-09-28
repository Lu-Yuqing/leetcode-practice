# Problem Link:https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROW or c == COL or board[r][c] != 'O':
                return
            # Turn O -> T
            board[r][c] = 'T'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # dfs capture unsurrounded regions O -> T
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O' and (r in [0, ROW - 1] or c in [0, COL - 1]):
                    dfs(r, c)
        # capture surrounded regions O -> X and turn T -> O
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

# T: O(mxn)
# S: O(mxn)