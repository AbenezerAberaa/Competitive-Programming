class Solution:
    
    def isValid(self, s):
        total_list = []
        container = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in container.values():
                total_list.append(char)
            elif char in container.keys():
                if total_list == [] or container[char] != total_list.pop():
                    return False
            else:
                return False
        return total_list == []