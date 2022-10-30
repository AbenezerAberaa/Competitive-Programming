# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)
        start.next = head
        current = start
        while current.next:
            next = current.next
            while next.next and next.next.val == next.val:
                next = next.next
            if current.next is not next:
                current.next = next.next
            else:
                current = current.next
        return start.next
        