class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        length = len(nums)
        minu = min(nums) - 1 
        maxu = max(nums) - minu
        result = [0] * length
        bit = [0] * (maxu+1)
        
        def count(a):
            c = 0;
            while a > 0:
                c += bit[a]
                a -= a & -a
            return c
        
        def insert(a):
            while a <= maxu:
                bit[a] += 1
                a += a & -a
            
        for i, a in enumerate(reversed(nums)):
            a = a - minu
            result[length-i-1] = count(a-1)
            insert(a)
            
        return result
