# Problem Link:https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minstack:
            self.minstack.append(min(value, self.minstack[-1]))
        else:
            self.minstack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


