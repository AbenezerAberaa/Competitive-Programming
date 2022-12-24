class Solution:
    def reverse(self, x: int) -> int:

        maxu = (2**31) - 1
        minu = -(2**31)
        sums = 0
        while x:
            digit = int(math.fmod(x, 10))
            sums = (sums * 10) + digit
            x = int(x/10)
        
        if sums > maxu or sums < minu:
            return 0
        return sums
