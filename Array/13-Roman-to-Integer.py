# Problem Link:https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: Greedy
class Solution:
    def romanToInt(self, s: str) -> int:
        mydict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s) - 1):
            if mydict[s[i]] < mydict[s[i + 1]]:
                total -= mydict[s[i]]
            else:
                total += mydict[s[i]]

        total += mydict[s[-1]]
        return total

# Time:O(n)
# S: O(1)
