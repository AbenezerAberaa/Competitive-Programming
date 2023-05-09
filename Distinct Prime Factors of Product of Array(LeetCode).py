class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primeSet = set()
        for num in nums:
            for i in range(2, int(sqrt(num)) + 1):
                while num % i == 0:
                    num //= i
                    primeSet.add(i)

            if num > 1: primeSet.add(num)

        return len(primeSet)
