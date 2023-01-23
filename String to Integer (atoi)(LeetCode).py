class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        res = 0
        negative = False
        if s[0] == "-":
            negative = True
        elif s[0] == "+":
            negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            res = ord(s[0]) - ord("0")

        print(res)
        for i in range(1, len(s)):
            if s[i].isnumeric():
                res = res*10 + (ord(s[i])- ord("0"))
                if negative and res >= 2147483648:
                    return -2147483648
                if not negative and res >= (2147483647):
                    return 2147483647
            else:
                break
        if negative:
            return -res
        else:
            return res

