class Solution:
    def countGoodSubstrings(self, s: str) -> int:
    
        count = 0
        for index in range(len(s)-3+1):
            new_s = s[index:index+3]
            if new_s[0] != new_s[1] and new_s[0] != new_s[2] and new_s[1] != new_s[2]:
                count += 1
        return count
