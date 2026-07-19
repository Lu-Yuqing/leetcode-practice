# Problem Link:https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga_map = {}
        for i in magazine:
            maga_map[i] = maga_map.get(i, 0) + 1

        for c in ransomNote:
            if c not in maga_map or maga_map[c] == 0:
                return False
            maga_map[c] -= 1

        return True

# Time:O(m+n)
# Space:0(m)

# method 2:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga = [0] * 26  # because we only have 26 english letter

        for i in magazine:
            maga[ord(i) - ord('a')] += 1

        for c in ransomNote:
            index = ord(c) - ord('a')
            if maga[index] == 0:
                return False
            maga[index] -= 1

        return True

# Time:O(m+n)
# Space:0(1)

