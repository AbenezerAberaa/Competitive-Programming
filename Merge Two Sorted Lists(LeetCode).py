# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        starter = prev

        
        while list1 and list2:
            if list1.val < list2.val:
                starter.next = list1
                list1 = list1.next
                
            else:
                starter.next = list2
                list2 = list2.next

            starter = starter.next
            
        if list1:
            starter.next = list1
        elif list2:
            starter.next = list2
                
        return prev.next

