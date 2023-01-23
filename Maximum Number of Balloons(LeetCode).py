class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        dic = Counter(text)
        print(dic)
        minu = float('inf')
        for char in "balloon":
            if char in "ban":
                minu = min(minu, dic[char])
            else:
                minu = min(minu, dic[char]//2)
        return minu
