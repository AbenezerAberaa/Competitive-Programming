class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        self.sortArray(left)
        self.sortArray(right)



        left_arr = 0
        right_arr = 0
        ink = 0

        while left_arr < len(left) and right_arr < len(right):
            if left[left_arr] < right[right_arr]:
                nums[ink] = left[left_arr]
                left_arr += 1
            else:
                nums[ink] = right[right_arr]
                right_arr += 1
            ink += 1
        while left_arr < len(left):
            nums[ink] = left[left_arr]
            left_arr += 1
            ink += 1
        while right_arr < len(right):
            nums[ink] = right[right_arr]
            right_arr += 1
            ink += 1
        
        return nums
        '''
        dic = Counter(nums)
        minu = min(nums)
        maxu = max(nums)
        arr = []
        for i in range(minu,maxu+1):
            arr.extend([i]*dic[i])
        return (arr)'''
