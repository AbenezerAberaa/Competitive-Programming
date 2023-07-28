class Solution:
    def tribonacci(self, n: int) -> int:
        orginal = [0, 1, 1]
        for n in range(3, n + 1):
            orginal[n % 3] = sum(orginal)
        return orginal[n % 3]
