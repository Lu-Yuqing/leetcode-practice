# Problem Link:https://leetcode.com/problems/zigzag-conversion/submissions/2039157945/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]

        current = 0
        godown = False

        for c in s:
            rows[current].append(c)

            if current == 0 or current == numRows - 1:  # when first row or last row, reverse the movement direction
                godown = not godown

            current += 1 if godown else -1

        return "".join([''.join(row) for row in rows])

# T: O(n)
# S: O(n)
