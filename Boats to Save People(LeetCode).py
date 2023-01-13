class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        left_ptr = 0
        right_ptr = len(people) - 1

        people.sort()
        boats_need = 0
        while left_ptr <= right_ptr:
            if people[left_ptr] + people[right_ptr] <= limit:
                left_ptr += 1
                right_ptr -= 1
            else:
                right_ptr -= 1
            boats_need += 1  
                
        return boats_need
