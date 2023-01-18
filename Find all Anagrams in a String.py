class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []

        container = [0] * 26
        for char in p:
            container[ord(char) - ord('a')] += 1

        left = 0
        right = 0
        while right < len(s):
            container[ord(s[right]) - ord('a')] -= 1
            while left <= right and container[ord(s[right]) - ord('a')] < 0:
                container[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1

        return result
