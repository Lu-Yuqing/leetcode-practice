# Problem Link:https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Calculate the product of all elements to the left of each index 'i'.
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # prefix * all elements to the right of 'i'.
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# Time: O(n)
# Space: total: O(n); extra: O(1)
