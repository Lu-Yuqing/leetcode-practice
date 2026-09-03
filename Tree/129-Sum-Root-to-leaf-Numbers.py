# Problem Link:https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: currsum = parentsum*10 + node.val
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, currsum):
            if not node:
                return 0

            currsum = currsum * 10 + node.val

            # reach the leaf
            if not node.left and not node.right:
                return currsum

            return dfs(node.left, currsum) + dfs(node.right, currsum)

        return dfs(root, 0)

# T:O(n)
# S:O(h)