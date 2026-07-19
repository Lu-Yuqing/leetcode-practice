# Problem Link:https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # temporary state: curr = 1, next = 0 -> -1; curr = 1, next = 1 -> 1; curr = 0, next = 0 -> 0; curr = 0, next = 1 -> 2

        nei = [(-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (-1, 1), (1, -1)]

        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                live = 0
                for dr, dc in nei:  # traverse neighbours
                    if 0 <= r + dr < m and 0 <= c + dc < n:
                        if abs(board[r + dr][c + dc]) == 1:
                            live += 1
                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        board[r][c] = - 1

                if board[r][c] == 0:
                    if live == 3:
                        board[r][c] = 2

        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 1
                if board[r][c] == -1:
                    board[r][c] = 0
# T:O(mxn)
# S: O(1)
