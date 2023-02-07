# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        firstHead = headA
        secondHead = headB
        while firstHead != secondHead:
            if not firstHead:
                firstHead = headB
            else:
                firstHead = firstHead.next
            if not secondHead:
                secondHead = headA
            else:
                secondHead = secondHead.next
        return secondHead
