class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()
        
        last  = len(heaters) - 1
        x1, x2 = 0, 0
        res = 0
        for y in houses:
            while x2 < last and y > heaters[x2]:
                x1, x2 = x2, x2+1
            d1,d2 = abs(heaters[x1] - y), abs(heaters[x2] - y)
            res   = max( res , min(d1,d2) )
        return res
