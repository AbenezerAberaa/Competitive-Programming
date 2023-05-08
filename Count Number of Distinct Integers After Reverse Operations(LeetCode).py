class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_array = []
        for item in nums:
            new_array.append(int(str(item)[::-1]))  
        nums.extend(new_array)                      
        return len(set(nums))   
