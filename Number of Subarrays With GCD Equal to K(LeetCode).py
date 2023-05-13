class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
            
        ans = 0
        size = len(nums)
        for i in range(size):
            g = nums[i]
            for j in range(i,size):
                g = gcd(g,nums[j])
                if g == k:
                    ans += 1
        return ans
