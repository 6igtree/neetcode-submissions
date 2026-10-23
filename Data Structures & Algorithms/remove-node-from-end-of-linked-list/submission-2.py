# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length = length + 1
        
        i = 0
        prev = None
        curr = head
        res = curr
        while curr:
            if length - n == 0:
                return head.next

            if i == length - n:
                prev.next = curr.next
            i = i + 1
            prev = curr
            curr = curr.next
        return head

