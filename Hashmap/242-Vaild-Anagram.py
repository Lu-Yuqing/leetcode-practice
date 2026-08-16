# Problem Link:https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        maps, mapt = [0]*26, [0]*26

        for i in range(len(s)):
            maps[ord(s[i])-ord('a')] += 1
            mapt[ord(t[i])-ord('a')] += 1

        return maps == mapt

# T: O(n)
# S: O(1)



