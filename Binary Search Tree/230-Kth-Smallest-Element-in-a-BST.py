# Problem Link:https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS in order traverse
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = None

        def traverse(node):
            if not node or self.res:
                return

            traverse(node.left)

            self.count -= 1
            if self.count == 0:
                self.res = node.val
                return self.res

            traverse(node.right)

        traverse(root)
        return self.res

# T: O(n)
# S: O(H)