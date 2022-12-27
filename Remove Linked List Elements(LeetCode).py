# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(next=head)
        starter = prev
        
        while head:
            nxt = head.next
            if head.val == val:
                starter.next = nxt
                head = nxt
            else:
                starter = head
                head = nxt
        return prev.next
            
