class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for digit in digits:
            string += str(digit)
        string = int(string) + 1
        string = str(string)
        result = []
        for char in string:
            result.append(int(char))
        return result
