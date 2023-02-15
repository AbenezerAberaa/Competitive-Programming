class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        k = min(k, len(nums))
        scores = [0 for i in nums] 
        scores[0] = nums[0]
        dq = deque([0])
        for index in range(1, len(nums)):
            val = nums[index]
              
            while dq and dq[0] < index - k:
                dq.popleft()
            scores[index] = scores[dq[0]] + val    
            while dq and scores[index] >= scores[dq[-1]]:
                dq.pop()
               
            dq.append(index)
        return scores[-1]
