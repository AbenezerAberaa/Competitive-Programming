class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        hash_dic = Counter(nums)
        rep, mis = None, None
        for index in range(len(nums)+1):
            if index not in hash_dic:
                mis = index
            if hash_dic[index] > 1:
                rep = index
        return [rep, mis]
            
