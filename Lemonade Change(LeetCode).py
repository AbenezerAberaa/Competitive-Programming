class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        dictionary = {5:0, 10:0, 20:0}

        for value in bills:
            if value == 5:
                dictionary[value] += 1
            if value == 10:
                if dictionary[5] >=1:
                    dictionary[5] -= 1 
                    dictionary[10] += 1
                else:
                    return False
            
            if value == 20:
                if dictionary[10] >= 1 and dictionary[5] >= 1:
                    dictionary[10] -= 1
                    dictionary[5] -= 1
                    
                elif dictionary[5] >= 3:
                    dictionary[5] -= 3
                else:
                    return False

                dictionary[20] += 1
        
        return True
                    
