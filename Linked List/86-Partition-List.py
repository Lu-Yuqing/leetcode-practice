# Problem Linkhttps://leetcode.com/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150

# method 1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)  # < x
        dummy2 = ListNode(-1)  # >= x
        p1 = dummy1
        p2 = dummy2
        curr = head
        while curr:
            if curr.val < x:
                p1.next = curr
                p1 = p1.next

            else:
                p2.next = curr
                p2 = p2.next

            curr = curr.next
        p2.next = None
        p1.next = dummy2.next

        return dummy1.next
# T: O(n)
# S: O(1)


