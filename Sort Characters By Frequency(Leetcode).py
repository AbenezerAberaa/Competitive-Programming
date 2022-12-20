class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = Counter(s)
        result = ''
        s = sorted(hash_map, key = lambda x: hash_map[x], reverse=True)

        for char in s:
            result += char * hash_map[char]
        return result
