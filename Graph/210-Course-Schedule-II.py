# Problem Link: https://leetcode.com/problems/course-schedule-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Method 1: BFS (Kahn)
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []
        while q:
            take = q.popleft()
            order.append(take)

            for nei in adj[take]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) == numCourses:
            return order
        else:
            return []

# T:O(V+E)
# S:O(V+E)