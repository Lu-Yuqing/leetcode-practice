# Problem Link:https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def calculate(number):
            total = 0
            while number:  # when number != 0
                digit = number % 10
                digit = digit ** 2
                total += digit
                number = number // 10
            return total

        while n not in seen:
            seen.add(n)
            n = calculate(n)
            if n == 1:
                return True

        return False

# T: O(logn)
# S: O(logn)



