# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(0,head)
        prev = res
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return res.next
            