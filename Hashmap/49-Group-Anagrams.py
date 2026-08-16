# Problem Link:https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

# method 1:
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for word in strs:
            key =''.join(sorted(word))
            maps[key].append(word)
        return list(maps.values())

T:O(N*klogk)
S:O(NK)



