# Problem Link:https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: 2 pointers
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        fast = dummy
        slow = dummy
        for _ in range(n): # fast pointer forward n steps
            fast = fast.next
        while fast.next: # When fast reaches the end, slow points to the node right before the target
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next

# T: O(n)
# S: o(1)
