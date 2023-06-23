class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ones = Counter()
        twos = Counter()
        threes = Counter()
        
        for num in nums:
            if ones[num - 1] > 0:
                ones[num - 1] -= 1
                twos[num] += 1
                continue
                
            if twos[num - 1] > 0:
                twos[num - 1] -= 1
                threes[num] += 1
                continue
                
            if threes[num - 1] > 0:
                threes[num - 1] -= 1
                threes[num] += 1
                continue
                
            ones[num] += 1
                
        if ones.total() > 0 or twos.total() > 0:
            return False
            
        return True
