class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        :type tree: List[int]
        :rtype: int
        """
        dict_maps = {}
        start = 0
        end = 0
        count = 0
        result = 0
        
        while end < len(fruits):
            dict_maps[fruits[end]] = dict_maps.get(fruits[end], 0) + 1
            if dict_maps[fruits[end]] == 1:
                count += 1
            end += 1  # end points to the next fruit
            while count > 2:
                dict_maps[fruits[start]] -= 1
                if dict_maps[fruits[start]] == 0:
                    count -= 1
                start += 1
            result = max(result, end - start)
        return result
        