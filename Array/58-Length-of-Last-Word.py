# Problem Link:https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

# method 1: #.split() can ignore leading and trail spaces and split by the spaces
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        return len(word[-1])

# Time: O(n)
# Space: O(n)

# method 2: pointer
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        # skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length

# T: O(n)
# S: o(1)
