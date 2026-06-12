# Problem Link:https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

# method 1: DP, bottom up
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [float('inf')]*n
        dp[n-1] = 0

        for i in range(n-2, -1, -1):
            maxstep = min(nums[i],n-1-i)
            for step in range(maxstep+1):
                count = 0
                dp[i] = min(dp[i], dp[step+i]+1)

        return dp[0]

# Time: O(n^2)
# Space: O(n)

# method 2: Greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0  # window: the res times jump, all possible position.
        n = len(nums)

        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)

            l = r + 1
            r = farthest
            res += 1
        return res

# Time: O(n)
# Space: O(1)

