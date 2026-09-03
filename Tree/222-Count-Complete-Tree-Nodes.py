# Problem Link:https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: BFS
from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return count
# T: O(n)
# S: O(n)

# method 2:
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_h, right_h = 0, 0
        curr = root
        while curr:
            left_h += 1
            curr = curr.left

        curr = root
        while curr:
            right_h += 1
            curr = curr.right

        if left_h == right_h:  # perfet binary tree, number of nodes = 2^h-1
            return 2 ** left_h - 1

        return 1 + self.countNodes(root.left) + self.countNodes(
            root.right)  # height of left != height of right -> the last level is not full.

# T: O(h^2) = O(log^2 n)
# S: O(h)

