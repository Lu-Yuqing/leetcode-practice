# Problem Link:https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/2119157703/?envType=study-plan-v2&envId=top-interview-150

# method 1: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # find the most right node in the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right

                prev.right = curr.right
                # move the entire left subtree to the right
                curr.right = curr.left
                # set left pointer to None
                curr.left = None

            curr = curr.right

# T: O(n)
# S: O(1)