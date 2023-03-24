class Solution:
    def commonChars(self, words: List[str]) -> List[str]:


        first_str_lst = list(words[0])
        for string in words:
            curr = []
            for char in string:
                if char in first_str_lst:
                    curr.append(char)
                    first_str_lst.remove(char)
            first_str_lst = curr
        
        return first_str_lst

