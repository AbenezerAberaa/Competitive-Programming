class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        short_str = min(strs, key=len)
        
        for index, character in enumerate(short_str):
            for other in strs:
                if other[index] != character:
                    return short_str[:index]
        return short_str
