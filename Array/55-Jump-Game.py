# Problem Link:https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

# method 1: recursion
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def canreach(i):  # starting from i, if it can reach the last index
            if i == n - 1:
                return True

            for step in range(1, nums[i] + 1):  # attempt all possible steps
                if canreach(i + step):
                    return True

            return False

        return canreach(0)  # start from the first position


# Time: O(max(nums)^n)
# Space: O(N)

# method 2: DP, bottom up
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):  # start form second to last element
            for step in range(1, nums[i] + 1):
                if i + step < n:
                    if dp[i + step] == True:
                        dp[i] = True
                        break

        return dp[0]
# Time: O(n^2)
# Space: O(n)

# method 3: Greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1  # initialize target = the last position

        for i in range(n - 2, -1, -1):  # start from the second to last position to see if it can reach the last.
            maxstep = nums[i]
            if i + maxstep >= target:
                target = i

        return target == 0  # if the final goal turn to be the first postion, we are able to jump to the end.

# Time: O(n)
# Space: O(1)