# Problem Link:https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = 0
        while start < len(nums):
            end = start
            # find the end of consecutive number
            while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end += 1
            if start == end:
                res.append(str(nums[start]))
            else:
                res.append(f'{nums[start]}->{nums[end]}')

            start = end + 1

        return res

# T: O(n)
# S: O(n)



