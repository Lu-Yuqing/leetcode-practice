# Problem Link:https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: two pointer
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # T: nlogn
        res = []

        def twosum(start, target):  # n for one time
            sub_res = []
            l = start
            r = len(nums) - 1

            while l < r:
                left, right = nums[l], nums[r]
                sum = left + right
                if sum > target:
                    while l < r and nums[r] == right:
                        r -= 1
                elif sum < target:
                    while l < r and nums[l] == left:
                        l += 1
                else:
                    sub_res.append([left, right])
                    while l < r and nums[l] == left:  # skip duplicate
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1

            return sub_res

        for i in range(len(nums)):  # n times twosum
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            pairs = twosum(i + 1, -nums[i])
            for pair in pairs:
                res.append([nums[i], pair[0], pair[1]])

        return res

# T: O(n^2)
# S: O(n)