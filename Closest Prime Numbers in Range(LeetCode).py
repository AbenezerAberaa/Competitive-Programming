class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        n = right+1
        isPrime = [0, 0] + [1] * (n-2)
        for i in range(2, int(math.sqrt(n))+1):
            if not isPrime[i]: continue
            for j in range(i*i, n, i):
                isPrime[j] = 0

        
        validPrimes = []
        for i in range(left, right+1):
            if isPrime[i]:
                validPrimes.append(i)

        
        gap = inf
        ans = None
        for i in range(len(validPrimes)-1):
            if validPrimes[i+1] - validPrimes[i] < gap:
                gap = validPrimes[i+1] - validPrimes[i]
                ans = [validPrimes[i], validPrimes[i+1]]
        
        return ans if ans else [-1, -1]
