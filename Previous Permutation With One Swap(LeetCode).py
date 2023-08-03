class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in reversed(range(len(arr)-1)):
            if arr[i] > arr[i+1]:
                break 
        else:
            return arr 
        
        new_i, val = i, 0
        for k in range(i+1, len(arr)): 
            if val < arr[k] < arr[i]: new_i, val = k, arr[k]
        
        arr[i], arr[new_i] = arr[new_i], arr[i]
        return arr 
