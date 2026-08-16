# Problem Link:https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: Greedy
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        pos = points[0][1]
        num = 1
        for i in range(1, len(points)):
            if points[i][0] > pos:
                num += 1
                pos = points[i][1]

        return num

# T: O(nlogn)
# S: O(1)
# Greedy: sort by increasing order of Xend; shoot the first at the end of first ballon. Iterate the rest, if start > last shoot position -> we need a new shoot.



