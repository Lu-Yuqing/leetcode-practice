# Problem Link:https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150

# method 1: 
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(-1, head)
        pre = dummy
        for _ in range(left - 1):  # pre move to left-1 position
            pre = pre.next

        cur = pre.next

        for _ in range(right - left):
            tep = cur.next  # temporary save the next point
            cur.next = tep.next
            tep.next = pre.next
            pre.next = tep

        return dummy.next

# T: O(n)
# S: O(1)
# Linked List rule:Save First, Break Second; the next pointer before modifying references: temp = node.next
# Why? Linked lists are single-pass chains. Once you break a next link without saving it first, all downstream nodes are permanently lost in memory.


