class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        begins = 0
        maximum = 0

        for value in range(1, len(s)):
            if (s[value] in s[begins:value]):
                maximum = len(s[begins:value]) if (len(s[begins:value]) > maximum) else maximum
                begins = s[begins:value].index(s[value]) + 1 + begins
            else:
                if (value == len(s) - 1):
                    maximum = max([maximum, len(s[begins:])])

        return maximum if (maximum != 0) else len(s)
