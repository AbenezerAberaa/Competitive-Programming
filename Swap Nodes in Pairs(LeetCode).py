# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        abs_nod_b4_head = ListNode(0, head)
        prev_ptr = abs_nod_b4_head
        curr_ptr = head

        while curr_ptr and curr_ptr.next:
            nxtcurr = curr_ptr.next.next
            secpair = curr_ptr.next

            secpair.next = curr_ptr
            curr_ptr.next = nxtcurr
            prev_ptr.next = secpair
            
            prev_ptr = curr_ptr
            curr_ptr = nxtcurr
        return abs_nod_b4_head.next
