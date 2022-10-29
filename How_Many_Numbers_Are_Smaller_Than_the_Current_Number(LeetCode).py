class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sortedNums = sorted(nums)
        index_dict = {}
        result_container = []
        
        for index in range(len(nums)):
            if sortedNums[index] not in index_dict:
                index_dict[sortedNums[index]] = index
                
        for index in nums:
            result_container.append(index_dict[index])
            
        return result_container