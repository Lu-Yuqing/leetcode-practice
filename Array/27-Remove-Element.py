# Problem Link:https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


# role of slow: 1. index 2. Counter: count the number of non-val elements
# Time: O(n)
# Space: O(1)

