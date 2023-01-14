class Solution:
    def maxArea(self, height: List[int]) -> int:
        #BRUTE FORCE METHOD
        '''result = 0
        for left in range(len(height)):
            for right in range(left, len(height)):
                area = (right - left) * min(height[left], height[right])
                result = max(result, area)
        return result'''
        #TWO POINTER
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
