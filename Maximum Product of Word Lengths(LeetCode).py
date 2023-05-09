class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dictionary = {}
        
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            
            dictionary[word] = mask
        
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if dictionary[words[i]] & dictionary[words[j]] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res
