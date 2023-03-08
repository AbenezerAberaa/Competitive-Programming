class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
    

        # for index, value in enumerate(arr):
        #     if value > arr[index+1]:
        #         return index
    
        left = 1
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
        return left -  1

