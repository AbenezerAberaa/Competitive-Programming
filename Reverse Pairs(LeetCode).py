class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def function(nums):
            if len(nums) < 2:
                return 0
            if len(nums) == 2:
                return 1 if nums[0] > 2*nums[1] else 0
            
            m = len(nums) // 2
            left = nums[:m]
            right = nums[m:]
            
            count = 0
            count += function(left)
            count += function(right)
            
            right.sort()
            left.sort()
            
            l, r = len(left) - 1, len(right) - 1
            while l >= 0 and r >= 0:
                if left[l] > 2*right[r]:
                    count += r + 1
                    l -= 1
                else:
                    r -= 1

            return count
        
        return function(nums)
