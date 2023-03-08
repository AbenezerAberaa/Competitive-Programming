class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def countDays(weight):
            days = 0
            index = 0
            while index < len(weights):
                _sum = 0
                while index < len(weights) and _sum + weights[index] <= weight:
                    _sum += weights[index]
                    index += 1
                days += 1
            return days
                
        left = max(weights)
        right = sum(weights)
        
        while left <= right:
            mid = left + (right - left)//2
            if countDays(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
