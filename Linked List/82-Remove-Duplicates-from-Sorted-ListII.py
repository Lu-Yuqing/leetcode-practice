# Problem Link:https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:  # duplicates appear
                x = curr.next.val  # duplicate value
                while curr.next and curr.next.val == x:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
# T: O(n)
# S: O(1)

