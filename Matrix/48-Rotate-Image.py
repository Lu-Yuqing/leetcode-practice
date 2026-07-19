# Problem Link:https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Horizontal Flip
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

# T: O(n^2)
# S: O(1)