class Solution:
    def longestWord(self, words: List[str]) -> str:

        words = sorted(words)
        curr = ''
        ws = set()
        for i in words:
            p = len(i)
            if p == 1 or i[:-1] in ws:
                if p > len(curr):
                    curr = i
                ws.add(i)
        return curr
