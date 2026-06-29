# Problem Link:https://leetcode.com/problems/minimum-size-subarray-sum/

# method 1: two pointer
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        smallest = float('inf')
        windowsum = 0

        for right in range(len(nums)):
            windowsum += nums[right]

            while windowsum >= target:
                smallest = min(smallest, right - left + 1)

                windowsum -= nums[left]
                left += 1

        if smallest == float('inf'):
            return 0
        else:
            return smallest

# T: O(n)
# S: O(1)
