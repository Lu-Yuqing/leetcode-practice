# Problem Link:https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: Bucket Sort
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0]*(n+1) # index & number of citation match

        for c in citations:
            if c >= n:
                count[n] += 1 # number of citation > total number of papers, add to the last bucket
            else:
                count[c] += 1
        total = 0
        for h in range(n, -1, -1):
            total += count[h] # accumulate citation >= h
            if total >= h:
                return h
        return 0

# Time: O(n)
# Space: O(n)
