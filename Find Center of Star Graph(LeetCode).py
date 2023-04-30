class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_node = edges[0][0]
        second_node = edges[0][1]

        if first_node == edges[1][0] or first_node == edges[1][1]:
            return first_node
        return second_node
