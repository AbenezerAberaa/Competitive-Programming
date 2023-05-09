class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if(n<2):
            return True
        n=bin(n)[2:]
        for each in range(1,len(n)):
            if(n[each]==n[each-1]):
                return False
        return True
