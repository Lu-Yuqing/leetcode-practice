# Problem Link:https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def intToRoman(self, num: int) -> str:
        mylist = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
                  ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]

        res = ''
        for sym, val in mylist:
            if num // val:
                count = num // val
                res += count * sym
                num = num % val

        return res

