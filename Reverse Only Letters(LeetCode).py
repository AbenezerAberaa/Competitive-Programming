class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while left < right:
            while left < right and s[left] not in alpha:
                left += 1
            while left < right and s[right] not in alpha:
                right -= 1
            if s[left] in alpha and s[right] in alpha:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        return "".join(s)
