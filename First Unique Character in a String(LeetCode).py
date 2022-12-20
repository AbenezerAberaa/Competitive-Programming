class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        lib_count = Counter(s)
        for index, value in enumerate(s):
            if lib_count[value] == 1:
                return index
        return -1

