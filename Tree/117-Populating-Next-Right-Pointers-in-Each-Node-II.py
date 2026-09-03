# Problem Link:https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

# T: O(n)
# S: O(n)

# method 2: pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root  # curr pointer used for tranversing the current level

        while curr:
            dummy = Node(-1)  # build the dummy head for next level
            tail = dummy
            while curr:  # traverse the current level connect the next level be the single direaction link
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            curr = dummy.next  # move down to the next levels head

        return root

# T:O(n)
# S: O(1)