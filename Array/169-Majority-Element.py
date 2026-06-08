# Problem Link:https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        for key, value in count.items():
            if value > n/2 :
                return key
# Space: O(n)
# Time: O(n)

# method 2:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = None, 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res

# Time: O(n)
# Space: O(1)