# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        t1 = head
        t2 = head

        while t2 and t2.next:
            t1 = t1.next
            t2 = t2.next.next

        front = None
        prev = None
        temp = t1.next
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        t1.next = None
        
        h2 = prev
        h1 = head
        h1next = None
        h2next = None
        while h1 and h2:
            h1next = h1.next
            h2next = h2.next

            h1.next = h2
            h2.next = h1next

            h1 = h1next
            h2 = h2next



        


        
