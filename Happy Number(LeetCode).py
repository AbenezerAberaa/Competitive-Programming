class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sums(number):
            total = 0
            while number > 0:
                digit = number % 10
                total += digit**2
                number = number // 10
            
            return total

        sets = set()
        while sums(n) not in sets:
            value = sums(n)
            if value == 1:
                return True
            else:
                sets.add(value)
                n = sums(n)
        return False
