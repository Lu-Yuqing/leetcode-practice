# Problem Link:https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

# method 1: Greedy
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        # sum(gas) >= sum(cost), we have enough gas to the end.
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start = i + 1

        return start

# Time: O(n)
# Space: O(1)

