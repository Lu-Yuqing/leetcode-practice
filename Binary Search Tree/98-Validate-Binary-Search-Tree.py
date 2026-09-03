# Problem Link:https://leetcode.com/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS in order traverse
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -float('inf')

        def traverse(node):
            if not node:
                return True

            if traverse(node.left) == False:
                return False

            if node.val <= self.prev:
                return False

            self.prev = node.val

            return traverse(node.right)

        return traverse(root)
# T: O(n)
# S: O(H)
