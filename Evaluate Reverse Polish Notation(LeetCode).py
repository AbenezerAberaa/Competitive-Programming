class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sums = 0
        for t in tokens:
            if t in set(['-','+','/','*']):
                x = stack.pop()
                y = stack.pop()
                if t=='+':
                    stack.append(x+y)
                elif t=='-':
                    stack.append(y-x)
                elif t=='/':
                    stack.append(int(y/x))
                elif t=='*':
                    stack.append(x*y)
            else:
                stack.append(int(t))
        return stack[0]
