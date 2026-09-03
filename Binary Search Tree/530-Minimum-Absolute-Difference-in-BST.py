# Problem Link:https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS in order traverse
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.diff = float('inf')
        self.prev = None

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            if self.prev is not None:
                self.diff = min(self.diff, node.val - self.prev)

            self.prev = node.val

            traverse(node.right)

        traverse(root)
        return self.diff

# T: O(n)
# S: O(n)