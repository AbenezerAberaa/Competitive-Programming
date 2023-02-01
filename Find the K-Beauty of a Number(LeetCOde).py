class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        
        count = 0
        left = 0
        for right in range(k-1,len(str_num)):
            store = str_num[left:right+1]
        
            if int(store)!=0 and num%int(store)==0:
                count += 1 
            left += 1
        return count

