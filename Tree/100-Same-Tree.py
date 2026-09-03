# Problem Link:https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS - recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# T: O(min(N, M))
# S: O(min(Hp, Hq))

# menthod 2: BFS - deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            node_p, node_q = queue.popleft()
            if not node_p and not node_q:
                continue
            if not node_p or not node_q or node_p.val != node_q.val:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True

# T: O(min(M,N))
# S: O(min(M,N))