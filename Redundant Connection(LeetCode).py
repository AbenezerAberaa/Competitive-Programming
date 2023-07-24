class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        self.parent = dict()
        
        for each in edges:
            
            first = self.find(each[0])
            second = self.find(each[1])
            if first == second:
                return each
            
            self.parent[first] = second
            
    def find(self, one_of):
        if one_of not in self.parent:
            return one_of
    
        return self.find(self.parent[one_of])
