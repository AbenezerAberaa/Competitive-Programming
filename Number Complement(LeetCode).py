class Solution:
    def findComplement(self, num: int) -> int:


        l = num.bit_length()
        print(l)
        mask = (1 << l) -1
        return num ^ mask
