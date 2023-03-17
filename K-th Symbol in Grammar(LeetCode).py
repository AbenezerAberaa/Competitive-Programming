class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def helper(n, k):

            if n == 1:
                return 0

            curr_len = 2**(n-1)
            mid = curr_len // 2
            if k <= mid:
                return helper(n-1, k)
            else:
                return 1 - helper(n-1, (k - mid))
        s = helper(n, k)
        return s

