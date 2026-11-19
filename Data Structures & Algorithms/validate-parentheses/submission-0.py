from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in {"{", "[", "("}:
                stack.append(c)
            elif c in {"}", "]", ")"}:
                if len(stack) == 0 or (stack[-1], c) not in {("{", "}"), ("[", "]"), ("(", ")")}:
                    return False
                stack.pop()
            else:
                raise ValueError(f"Unexpected character {c}")
        return len(stack) == 0
