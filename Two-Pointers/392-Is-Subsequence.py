# Problem Link:https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: two pointer
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1

            p2 += 1

        return p1 == len(s)

# T: O(len(t))
# S: O(1)


# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence.
# Method: preprocessing t into index map, using binary search to find the next valid charcter position.

from collections import defaultdict
import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = defaultdict(list)
        for i, char in enumerate(t):
            pos[char].append(i)

        curr_t_idx = -1  
        for char in s:
            if char not in pos:
                return False

            idx_list = pos[char]
            insert_pos = bisect.bisect_right(idx_list, curr_t_idx)

            if insert_pos == len(idx_list):
                return False

            curr_t_idx = idx_list[insert_pos]

        return True

# preprocessing T: O(len(t)), S: O(len(t)
# check s: O(len(s)log(len(t))