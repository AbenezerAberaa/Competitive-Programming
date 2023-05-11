class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        
        result = []
        for i in range(1, 4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    if k < n:
                        s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                        if self.isValid(s1) and self.isValid(s2) and self.isValid(s3) and self.isValid(s4):
                            result.append(".".join([s1, s2, s3, s4]))
        
        return result
    
    def isValid(self, s: str) -> bool:
        n = int(s)
        return 0 <= n <= 255 and str(n) == s
