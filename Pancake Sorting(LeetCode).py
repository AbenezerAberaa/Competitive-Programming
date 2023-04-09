class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        new_arr = []
        
        for index in range(length):
            maxu = max(arr[:length - index])
            maxu_index = arr.index(maxu) + 1
            arr[:maxu_index] = reversed(arr[:maxu_index])
            new_arr.append(maxu_index)
            
            arr[:length - index] = reversed(arr[:length - index])
            new_arr.append(length - index)
        return new_arr
