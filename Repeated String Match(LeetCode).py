class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        len_a = len(a)
        len_b = len(b)
        if not len_b:
            return 0
        mul = -(-len_b//len_a)
        
        reps = a*mul
        if b in reps:
            return mul
        elif b in reps+a:
            return mul+1
        
        return -1
