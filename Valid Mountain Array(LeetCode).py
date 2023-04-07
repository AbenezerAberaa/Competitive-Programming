class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        pointer = 1
        while pointer < len(arr) and arr[pointer] > arr[pointer-1]:
            pointer += 1
        
        if pointer == 1 or pointer == len(arr):
            return False
        while pointer < len(arr) and arr[pointer] < arr[pointer-1]:
            pointer += 1
        if pointer == len(arr):
            return True
        else:
            return False
