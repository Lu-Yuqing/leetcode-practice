# Problem Link: https://leetcode.com/problems/clone-graph/?envType=study-plan-v2&envId=top-interview-150

# method 1: DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        # give the curr, return the clone of current node
        def dfs(curr):
            if curr in visited:
                return visited[curr]

            clone = Node(curr.val)
            visited[curr] = clone

            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)
# T: O(V+E)
# S: O(V)