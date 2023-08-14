class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        for i in range(len(requests), 0 ,-1):
            for j in itertools.combinations(range(len(requests)), i):
                arr = [0] * n
                for k in j :
                    arr[requests[k][0]] -= 1
                    arr[requests[k][1]] += 1
                if not any(arr):
                    return i
        return 0
