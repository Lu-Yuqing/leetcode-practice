# Problem Link:https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                a = stack.pop()
                b = stack.pop()

                if i == "+":
                    stack.append(b+a)
                elif i == "-":
                    stack.append(b-a)
                elif i == "*":
                    stack.append(b*a)
                elif i == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[-1]


