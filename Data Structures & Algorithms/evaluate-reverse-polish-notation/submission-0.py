from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                if len(stack) < 2:
                    raise ValueError("Invalid operation")
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if token == "+":
                    result = operand_1 + operand_2
                elif token == "-":
                    result = operand_1 - operand_2
                elif token == "*":
                    result = operand_1 * operand_2
                else:
                    result = int(operand_1 / operand_2)
                stack.append(result)
            else:
                stack.append(int(token))
        if len(stack) != 1:
            raise ValueError("Invalid operation")
        return stack.pop()
