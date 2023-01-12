class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        len_po = len(popped)
        i = 0
        for value in pushed:
            stack.append(value)
            while stack and i < len_po and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return stack == []
