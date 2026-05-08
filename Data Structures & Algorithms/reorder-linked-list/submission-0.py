# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head:
            curr = head
            nodes = []
            while curr.next != None:
                nodes.append(curr)
                curr = curr.next
            nodes.append(curr)

            curr = head
            for i in range(1,(len(nodes)//2)+1):
                curr.next = nodes[len(nodes)-i]
                curr = curr.next
                curr.next = nodes[i]
                curr = curr.next
            if len(nodes)%2 == 0:
                curr.next = nodes[len(nodes)-i]
                curr = curr.next
            curr.next = None