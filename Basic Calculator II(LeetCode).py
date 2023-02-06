class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        prevNum = 0
        currNum = 0
        operator = '+'

        for index, val in enumerate(s):
            if val.isdigit():
                currNum = currNum * 10 + int(val)
            if not val.isdigit() and val != ' ' or index == len(s) - 1:
                if operator == '+' or operator == '-':
                    ans += prevNum
                    prevNum = currNum if operator == '+' else -currNum
                elif operator == '*':
                    prevNum = prevNum * currNum
                elif operator == '/':
                    if prevNum < 0:
                        prevNum = math.ceil(prevNum / currNum)
                    else:
                        prevNum = prevNum // currNum
                operator = val
                currNum = 0

        return ans + prevNum
