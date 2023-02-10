class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        left = 0
        for right in range(len(s)):
            if left < len(g):
                if g[left] <= s[right]:
                    left += 1
        return left
