class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dic = Counter(s)
        
        for char in t:
            if char not in dic:
                return char
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1


