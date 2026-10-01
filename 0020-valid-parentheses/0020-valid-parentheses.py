class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack