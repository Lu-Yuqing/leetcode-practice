# Problem Link:https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        mapp, maps = {}, {}
        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            c1, w1 = pattern[i], s[i]
            if (c1 in mapp and mapp[c1] != w1) or (w1 in maps and maps[w1] != c1):
                return False


            mapp[c1] = w1
            maps[w1] = c1
        return True

# T: O(n)
# S: O(n)



