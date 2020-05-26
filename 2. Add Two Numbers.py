# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        mul = 1
        while l1 or l2:
            if l1:
                num1 += mul*l1.val
                temp = l1
                l1 = l1.next
                del(temp)
            if l2:
                temp = l2
                num2 += mul*l2.val
                l2 = l2.next
                del(temp)
            mul*=10
        
        s = num1+num2
        rem = s%10
        s = s//10
        res = ListNode(rem,None)
        temp = res
        while s != 0:
            rem = s%10
            s = s//10
            temp.next = ListNode(rem,None)
            temp = temp.next
        
        
        return res
            