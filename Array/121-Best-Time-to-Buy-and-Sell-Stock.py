# Problem Link:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minp = prices[0]

        for price in prices:
            maxprofit = max(maxprofit, (price - minp))
            minp = min(minp, price)
        return maxprofit

# Time: O(n)
# Space: O(1)