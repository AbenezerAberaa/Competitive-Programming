class Solution:
    def addDigits(self, num: int) -> int:
        sums = 0
        while num > 0:
            sums += num % 10
            num //= 10 
        if sums < 10:
            return sums
        return self.addDigits(sums)

        

