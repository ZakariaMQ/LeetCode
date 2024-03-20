class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)

        return not stack

# submition link:
# https://leetcode.com/problems/valid-parentheses/solutions/4900700/beats-96-of-other-submissions-runtime-details-included