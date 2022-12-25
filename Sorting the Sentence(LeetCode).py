class Solution:
    def sortSentence(self, s: str) -> str:
        array = s.split()
        array.sort(key=lambda word: int(word[-1]))
        result = []
        for word in array:
            result.append(word[:-1])
        return " ".join(result)
           
