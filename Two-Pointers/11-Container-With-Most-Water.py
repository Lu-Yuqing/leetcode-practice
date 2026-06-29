# Problem Link:https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

# method 1: two pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return area

# T:O(n)
# S:O(1)