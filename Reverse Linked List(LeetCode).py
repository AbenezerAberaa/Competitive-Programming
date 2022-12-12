# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        self.prev = None
        self.curr = head
        self.next = None

        while(self.curr):
            next = self.curr.next
            self.curr.next = self.prev
            self.prev = self.curr
            self.curr = next
        return self.prev
