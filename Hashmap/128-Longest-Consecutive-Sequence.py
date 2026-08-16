# Problem Link:https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:create hashset
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) #create hashset, O(1) check if the number exist

        longest = 0 # need consider empty list situation

        for num in s:
            if num-1 not in s: # identify if this number is the start
                curr = num
                curr_len = 1

                while curr + 1 in s:
                    curr_len += 1
                    curr += 1
                longest = max(longest, curr_len)
        return longest

# T:O(n)
# S: O(n)



