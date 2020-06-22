# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        temp = ListNode(0)
        temp.next = head
        curr = temp
        while curr and curr.next and curr.next.next:
            n1, n2 = curr.next, curr.next.next
            n3 = n2.next
            curr.next, n2.next, n1.next = n2, n1, n3
            curr = n1
        return temp.next