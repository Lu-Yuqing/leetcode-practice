# Problem Link:https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        slow, fast = 2, 2  # start from the 3rd element, fast represents next checked element, slow represents next writable area

        while fast < n:
            if nums[fast] != nums[slow - 2]:  # each number duplicate <= 2, the left of slow is processed and safe area
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow

# Time: O(n)
# Space: O(1)
