# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

# method 1: 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]
        for i in range(len(reference)):
            for s in strs[1:]:
                if i == len(s) or s[i] != reference[i]:
                    return reference[:i]

        return reference

# Time:O(S), sum of all characters
# Space:O(1)
