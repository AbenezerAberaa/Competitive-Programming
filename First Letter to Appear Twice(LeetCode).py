class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_map = {}
        for value in s:
            if value not in hash_map:
                hash_map[value] = 1
            else:
                return value
