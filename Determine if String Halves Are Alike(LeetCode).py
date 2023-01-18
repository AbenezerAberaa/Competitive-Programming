class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        count = 0
        for index in range(len(s)//2):
            if s[index] in vowels:
                count += 1
        count1 = 0
        for index in range(len(s)//2,len(s)):
            if s[index] in vowels:
                count1 += 1
        return count == count1
