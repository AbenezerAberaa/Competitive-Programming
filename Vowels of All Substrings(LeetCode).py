class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        n = len(word)
        for index in range(n):
            if word[index] in "aeiou":
                count += (n-index)*(index+1)
                print(count)
        return count
