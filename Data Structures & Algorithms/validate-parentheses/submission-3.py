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
            if stack and char == ref[stack[-1]]:
                stack.pop()
            else:
                return False

        if not stack:
            return True
        else:
            return False

