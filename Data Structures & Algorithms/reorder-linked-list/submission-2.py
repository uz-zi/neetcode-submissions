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

        cur = t1.next
        prev = None
        nxt = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        h2 = prev
        h1 = head
        t1.next = None
        temp1 = None
        temp2 = None
        while h1 and h2:
            temp1 = h1.next
            temp2 = h2.next
            h1.next = h2
            h2.next = temp1

            h1 = temp1
            h2 = temp2
            

            




