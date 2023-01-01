class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        count_dic = Counter(nums)
        maxu = max(nums)
        result = 0
        prev = -1
        for value in range(maxu+1):
            freq = count_dic[value]
            if freq > 0:
                totalMoves = 0
                maxMove = freq - 1
                totalMoves = maxMove * (maxMove + 1) // 2
                maxNum = value + maxMove


                if value <= prev:
                    totalMoves += freq * (prev - value + 1)
                    maxNum += (prev - value + 1)
                result += totalMoves
                prev = maxNum
        return result
