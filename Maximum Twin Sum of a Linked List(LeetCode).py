# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        array = []
        while(head):
            array.append(head.val)
            head = head.next
        
        sums = 0
        for each in range(len(array)):
            sums = max(sums, array[each]+array[len(array) - 1 - each])
            
        return sums

