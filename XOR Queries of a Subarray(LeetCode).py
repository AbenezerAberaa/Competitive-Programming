class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        xors = [0] * (len(arr) + 1)

        for index, value in enumerate(arr):
            xors[index + 1] ^= xors[index] ^ value

        for l, r in queries:
            ans.append(xors[l] ^ xors[r + 1])

        return ans
