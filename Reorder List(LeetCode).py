# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        
        fast, slow = head, head   
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next      
        mid = slow
        
        
        prev, cur = None, mid
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        head_of_second_rev = prev
    
        
        first, second = head, head_of_second_rev 
        while second.next:
            
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop
