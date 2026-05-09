# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        curr = l1
        while curr.next is not None:
            num1 = str(curr.val) + num1
            curr = curr.next
        num1 = str(curr.val) + num1

        curr = l2
        while curr.next is not None:
            num2 = str(curr.val) + num2
            curr = curr.next
        num2 = str(curr.val) + num2
        print(num1, num2)
        sum = str(int(num1) + int(num2))
        curr = ListNode(sum[0], None)
        left = 1
        while left != len(sum):
            before = ListNode(sum[left], curr)
            curr = before
            left += 1
        return curr