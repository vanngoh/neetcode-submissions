class Solution:
    def isValid(self, s: str) -> bool:

        ref = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for char in s:
            # Push the open bracket into stack
            if ref.get(char, None):
                stack.append(char)
                continue

            # Check the correct close bracket, 
            # pop the open bracket from stack
            if len(stack) > 0 and char == ref[stack[-1]]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False

