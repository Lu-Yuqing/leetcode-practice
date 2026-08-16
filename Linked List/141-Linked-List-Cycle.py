# Problem Link:https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: 2 pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# T: O(n)
# S: O(1)


