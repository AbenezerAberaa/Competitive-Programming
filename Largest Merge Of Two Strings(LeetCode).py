class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        left1 = 0
        left2 = 0
        ans = ""
        while left1 < len(word1) and left2 < len(word2):
            
            if word1[left1] < word2[left2]:
                ans += word2[left2]
                left2 += 1
            elif word1[left1] > word2[left2]:
                ans += word1[left1]
                left1 += 1
            else:
                if word1[left1:] > word2[left2:]:
                    ans += word1[left1]
                    left1 += 1
                else:
                    ans += word2[left2]
                    left2 += 1
        
        while left1 < len(word1):
            ans += word1[left1]
            left1 += 1
            

        while left2 < len(word2):
            ans += word2[left2]
            left2 += 1
           
        return ans
