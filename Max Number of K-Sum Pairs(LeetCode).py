class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        count = 0 
        
        for num in nums:
            target = k - num
            
            if dic[target] > 0:
                dic[target] -= 1
                count += 1
            else:
                dic[num] += 1
                
        return count 
