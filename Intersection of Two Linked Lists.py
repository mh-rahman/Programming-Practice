# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_1 = headA
        p_2 = headB
        
        if p_1 == p_2: return p_1
        
        try:
            while p_1 and p_2:
                p_1 = p_1.next
                p_2 = p_2.next
                
            # if not p_1 and not p_2: return None
            
            print(p_1,p_2)
            
            if not p_1:
                small_list = headA
                ahead = headB
                behind = p_2
                print("if1")
            else:
                small_list = headB
                ahead = headA
                behind = p_1
                print("else1")
            
            while behind:
                behind = behind.next
                ahead = ahead.next
            
            behind = small_list
            
            while ahead != behind:
                behind = behind.next
                ahead = ahead.next
                
            return ahead
                
        except:
            return None
        
        
        
        