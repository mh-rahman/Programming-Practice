# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        # add an node in front to avoid edge cases
        newHead = ListNode(0,head)
        
        i = 1
        node_l, node_m = newHead, head
        
        while i < m:
            node_l = node_m
            node_m = node_m.next
            i += 1
            
        
        curr = node_m
        prev = None
        
        while i <= n:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1
            
        node_m.next = curr
        node_l.next = prev
        
        return newHead.next
        
        
        
        
        
        
    def oldreverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # new_head = ListNode()
        temp = None
        i = 1
        while i < m:
            temp = head
            head = head.next
            i += 1
        curr = temp
        print(curr.val)
        while head:
            print(head.val)
            temp2 = head.next
            head.next = temp
            temp = head
            head = temp2
        
        return temp