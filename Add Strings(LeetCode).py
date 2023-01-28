class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = len(num1) - 1
        b = len(num2) - 1
        carry = 0

        result = ""
        while a >= 0 or b >= 0:
            i, j = 0, 0
            if a >= 0:
                i = ord(num1[a]) - ord("0")
                a -= 1
            if b >= 0:
                j = ord(num2[b]) - ord("0")
                b -= 1
            temp = i + j + carry
            if temp > 9:
                carry = 1
            else:
                carry = 0
            result = str(temp)[-1] + result 
        if carry:
            result = "1" + result
        return result
