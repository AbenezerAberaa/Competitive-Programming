class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        max_val = int(sqrt(c))
        sets = set()
        for val in range(max_val+1):
            sets.add(val*val)
        for val in sets:
            new_val = c - val
            if new_val in sets:
                return True
        return False
