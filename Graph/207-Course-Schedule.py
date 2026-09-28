# Problem Link: https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)


        # 0-> unvisited 1-> in the current path 2-> no cycle
        state = [0]*numCourses

        def no_cycle(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1
            for nei in graph[node]:
                if not no_cycle(nei):
                    return False

            state[node] = 2
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not no_cycle(i):
                    return False
        return True
# T: O(V+E)
# S: O(V+E)

# Method 2: BFS (Kahn)
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()
        complete = 0
        for i in range(numCourses):
            if indegree[i] == 0:  # no prerequisite needed
                q.append(i)

        while q:
            take = q.popleft()
            complete += 1
            for nei in adj[take]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return complete == numCourses

# T:O(V+E)
# S:O(V+E)