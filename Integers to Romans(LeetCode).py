class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

        divisor = 1
        while num >= divisor:
            divisor *= 10
  
        divisor /= 10
   
        result = ""
  
        while num:
            first_digit = int(num / divisor)
  
            if first_digit <= 3:
                result += (hash_map[divisor] * first_digit)
                
            elif first_digit == 4:
                result += (hash_map[divisor] + hash_map[divisor * 5])
                
            elif 5 <= first_digit <= 8:
                result += (hash_map[divisor * 5] + (hash_map[divisor] * (first_digit - 5)))
                
            elif first_digit == 9:
                result += (hash_map[divisor] + hash_map[divisor * 10])
                
            
            num = (num % divisor)
            divisor /= 10
          
        return result
