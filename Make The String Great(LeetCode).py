class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            stack.append(char)
        
            if len(stack) >= 2 and stack[-1].lower() == stack[-2].lower() and stack[-1] != stack[-2]:
                stack.pop()
                stack.pop()
        return "".join(stack)
