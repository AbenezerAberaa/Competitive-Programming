# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = []
        self.curr = head
        
        
        while(self.curr is not None):
            reverse.append(self.curr.val)
            self.curr = self.curr.next
        return reverse == reverse[::-1]

