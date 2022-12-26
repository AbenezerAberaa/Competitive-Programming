class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        
        hash_map = Counter(magazine)
        for char in ransomNote:
            if char not in hash_map:
                return False
            if hash_map[char] <= 0:
                return False
            hash_map[char] -= 1
        return True   
