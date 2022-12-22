# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        self.curr = head
    
        while(self.curr):
            while self.curr.next and self.curr.val == self.curr.next.val:
                self.curr.next = self.curr.next.next
            self.curr = self.curr.next
        return head
