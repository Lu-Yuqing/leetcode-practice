# Problem Link:https://leetcode.com/problems/basic-calculator-ii/description/

# method 1:
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        presign = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)  # assemble muti digit number

            if (not c.isdigit() and c != " ") or i == len(s) - 1:
                if presign == '+':
                    stack.append(num)
                elif presign == '-':
                    stack.append(-num)
                elif presign == '*':
                    stack.append(stack.pop() * num)
                elif presign == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))

                presign = c
                num = 0
        return sum(stack)


