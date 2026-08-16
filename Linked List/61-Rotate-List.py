# Problem Link:https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: connect the linked list to be a circle, then find the cut postion.
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # count the length
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next

        k %= n
        if k == 0:
            return head

        # be a circle
        tail.next = head

        # find the new tail
        newtail = head
        for _ in range(n - 1 - k):
            newtail = newtail.next

        newhead = newtail.next
        newtail.next = None

        return newhead

# T: O(n)
# S: O(1)

