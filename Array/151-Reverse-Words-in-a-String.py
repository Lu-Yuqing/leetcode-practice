# Problem Link:https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: built-in function
class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        return " ".join(reversed(word))

# T: O(n)
# S: O(n)

# method 2: two pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # remove leading and trailing white spaces
        i = len(s) - 1
        res = []

        while i >= 0:
            # find the end of the word
            while i >= 0 and s[i] == " ":
                i -= 1

            end = i
            # find the start of the word
            while i >= 0 and s[i] != " ":
                i -= 1

            start = i

            if end >= 0:
                res.append(s[start + 1: end + 1])

        return " ".join(res)

# T:O(n)
# S:O(n)


