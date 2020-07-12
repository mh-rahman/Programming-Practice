# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        s_half, slow, fast = [], head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        while temp:
            s_half.append(temp)
            temp = temp.next
        
        if not s_half:
            return
        
        s_half[0].next = slow.next = None
        
        while s_half:
            node = s_half.pop()
            temp = head.next
            head.next = node
            node.next = temp
            head = temp
        
        return