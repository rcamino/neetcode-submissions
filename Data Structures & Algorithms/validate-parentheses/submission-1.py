from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif c == "}" or c == "]" or c == ")":
                if len(stack) == 0:
                    return False
                cc = stack.pop() + c
                if not (cc == "{}" or cc == "[]" or cc == "()"):
                    return False
            else:
                raise ValueError(f"Unexpected character {c}")
        return len(stack) == 0
