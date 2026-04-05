# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totallen = 0
        curr = head
        while curr is not None:
            totallen += 1
            curr = curr.next
        
        index = totallen - n
        if index == 0:
            return head.next
        
        curr = head
        currindex = 0
        while index-1 != currindex:
            curr = curr.next
            currindex += 1
        curr.next = curr.next.next
        return head
