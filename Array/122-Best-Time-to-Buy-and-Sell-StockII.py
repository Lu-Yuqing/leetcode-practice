# Problem Link:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        high = prices[0]
        low = prices[0]
        n = len(prices)
        profit = 0

        while i < n-1:
            # go down to see where to buy (buy in low)
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            low = prices[i]

            # go up to see where to sell (sell in high)
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]

            profit += high - low

        return profit

# Time: O(n)
# Space: O(1)