class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:


        left = 0
        right = len(arr) - k
        value = x
        while left < right:
            mid = (left + right) // 2
            if value - arr[mid] > arr[mid+k] - value:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
