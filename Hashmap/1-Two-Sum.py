# Problem Link:https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i, num in enumerate(nums):
            rest = target - nums[i]
            if rest in mymap:
                return[mymap[rest], i]
            else:
                mymap[num] = i
# T:O(n)
# S:O(n)



