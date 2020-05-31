# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None
        
        ahead = head
        behind = head
        count = 1
        flag = False
        while ahead.next:
            ahead = ahead.next
            if count > n:
                behind = behind.next
            count += 1
        
        if count > n:
            flag = True
        if flag:
            behind.next = behind.next.next
        else:
            head = head.next
        
        return head
        