# Problem Link:https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS - recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node1, node2):
            # base case
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

        return isMirror(root.left, root.right)

# T:O(n)
# S: O(h)

