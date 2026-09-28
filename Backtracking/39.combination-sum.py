#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        candidates.sort() # for pruning

        def backtrack(path, start, remain):
            if remain == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remain: # Pruning: subsequent numbers are larger
                    break

                path.append(num)
                # pass 'i' because the same element can be reused
                backtrack(path, i, remain-num)
                path.pop()
            
        backtrack(path, 0, target)
        return res


        
# @lc code=end

