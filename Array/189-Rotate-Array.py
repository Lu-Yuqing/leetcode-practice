# Problem Link:https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # handle when k > list length
        res = [0]*n # initialize res with same size, so indices exist
        for i in range(n):
            if i + k < n:
                res[i+k] = nums[i]
            else:
                res[(i+k)%n] = nums[i]
        nums[:] = res # modify nums in-place using slice assignment

# Time: O(n)
# Space: O(n)

# method 2: reverse the entire array -> reverse the first k elements -> reverse the remaining n-k elements
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        reverse(0, n - 1)  # reverse whole
        reverse(0, k - 1)  # reverse the first k elements
        reverse(k, n - 1)  # reverse the rest

# Time: O(n)
# Space: O(1)