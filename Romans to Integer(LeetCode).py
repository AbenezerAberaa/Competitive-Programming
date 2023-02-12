class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sums = 0
        index = len(s) -1
        for index in range(len(s)):
            if index > 0 and hash_map[s[index]] > hash_map[s[index-1]]:
                sums += hash_map[s[index]] - 2 * hash_map[s[index - 1]]
            else:
                sums += hash_map[s[index]]
            
                     
        return sums
