# Problem Link:https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        element = path.split('/')
        stack = []
        for i in element:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        res = "/" + "/".join(stack)

        return res

# T: O(n)
# S: O(n)


