# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        temp = slow.next
        nexxt =  None

        while temp:
            nexxt = temp.next
            temp.next = prev
            prev = temp 
            temp = nexxt
        
        slow.next = None

        t1 = head
        t2 = prev
        t1next = None
        t2next = None

        while t1 and t2:
            t1next = t1.next
            t2next = t2.next

            t1.next = t2
            t2.next = t1next

            t1 = t1next
            t2 = t2next
        
        

        




        