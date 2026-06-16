# Problem Link:https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Merge from back to front to prevent data overwriting
        x = m - 1
        y = n - 1
        p = len(nums1) - 1

        while x >= 0 and y >= 0:
            if nums1[x] >= nums2[y]:
                nums1[p] = nums1[x]
                x -= 1
            else:
                nums1[p] = nums2[y]
                y -= 1
            p -= 1

        while y >= 0:
            nums1[p] = nums2[y]
            y -= 1
            p -= 1

# Time: O(m+n)
# Space: O(1)

