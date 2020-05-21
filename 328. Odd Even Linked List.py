# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = head.next
        
        end1 = odd
        end2 = even
        
        while end2.next.next:
            end1.next = end2.next
            end1 = end1.next
            end2.next = end2.next.next
            end2 = end2.next
            if not end2.next:
                break
            
        if end2.next:
            end1.next = end2.next
            end2.next = None
            end1 = end1.next
            
        end1.next = even

            
        return odd
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        