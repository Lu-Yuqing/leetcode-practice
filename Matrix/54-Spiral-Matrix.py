# Problem Link:https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []

        while left <= right and top <= bottom:
            # left -> right
            for i in range(left, right + 1):
                # tranverse the top row left -> right
                res.append(matrix[top][i])
                # move top boundry down
            top += 1

            # top -> bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # handle non-square matrices, prevent duplicate append
            if top <= bottom:
                # right -> left
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # handle non-square matrices, prevent duplicate append
            if left <= right:
                # bottom -> top
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

# T:O(mxn)
# S: O(1)