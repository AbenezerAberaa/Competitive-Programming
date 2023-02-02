class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = collections.Counter(arr)
        mid = len(arr)//2
        result = 0
        for i , j in sorted(dic.items(), key=lambda x:-x[1]):
            if mid>0:
                result += 1
                mid -= j
            else:
                break
        return result
