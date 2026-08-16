# Problem Link:https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res

# T: O(nlogn)
# S: O(n)


