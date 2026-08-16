# Problem Link:https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        map = {}  # old:new

        # build map
        while curr:
            newNode = Node(x=curr.val)
            map[curr] = newNode
            curr = curr.next

        # connect next and random
        curr = head
        while curr:
            map[curr].next = map[curr.next] if curr.next else None
            map[curr].random = map[curr.random] if curr.random else None
            curr = curr.next

        return map[head]

# T: O(n)
# S: O(n)


