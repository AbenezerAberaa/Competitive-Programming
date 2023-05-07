class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.m = 0
        def solve(com,arr):
            if(len(com) == len(set(com))):
                self.m = max(self.m,len(com))
            else:
                return
            for i in range(len(arr)):
                solve(com+"".join(arr[i]),arr[i+1:])
        solve("",arr)
        return self.m
