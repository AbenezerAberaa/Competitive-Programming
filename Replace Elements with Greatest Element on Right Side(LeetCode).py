class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:


        maxu = -1
        for index in range(len(arr)-1, -1, -1):
            maxu = max(maxu, arr[index] if arr[index] else maxu)
            arr[index] = maxu
        arr.append(-1)
        return(arr[1:])
