class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens)-1
        ans = 0
        score = 0
        while left<=right:
            if score>=0 and power>=tokens[left]:
                power-=tokens[left]
                left+=1
                score += 1
                ans = max(ans,score)
            elif score>=1 and power<tokens[left]:
                power += tokens[right]
                score -=1
                right-=1
            else:
                return 0
        return ans
