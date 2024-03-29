class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        freq = {}
        long_sub = 0
        
        for r in range(len(s)):
            
            if not s[r] in freq:
                freq[s[r]] = 0
                
            freq[s[r]] += 1
            
            j = max(freq.values())
            
            if  r - l + 1 - j <= k:
                long_sub = max(long_sub,  r - l + 1)
                
            else:
                freq[s[l]] -= 1
                
                if not freq[s[l]]:
                    freq.pop(s[l])
                    
                l += 1
        
        return long_sub
        
