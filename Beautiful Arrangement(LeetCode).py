class Solution:
    def countArrangement(self, n: int) -> int:
        num_list = [i+1 for i in range(n)]

        count = 0
        def search_for(rest_nums, curr_nums):
            if not rest_nums:
                
                nonlocal count
                count +=1
                return

            i = len(curr_nums) + 1
            for j in range(len(rest_nums)):
                n = rest_nums[j]
                if (n % i)==0 or (i % n)==0:
                   
                    search_for(rest_nums[:j]+rest_nums[j+1:], curr_nums + [n])


        search_for(num_list, [])
        return count
