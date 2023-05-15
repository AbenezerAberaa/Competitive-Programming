class Solution:
    def minSteps(self, n: int) -> int:

        res = float(inf)
        stack = [(1, 0, 0)]

        while stack:
            num, ops, last = stack.pop()
            if num>n:
                continue
            if num==n:
                res = min(res,ops)
                continue
            if num>1:
                stack.append((num+last, ops+1, last))
            stack.append((num*2, ops+2, num))
        return res
