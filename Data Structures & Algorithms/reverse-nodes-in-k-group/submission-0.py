# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth == None:
                    return dummy.next
            
            group_next = kth.next

            prev = group_next
            cur = group_prev.next

            while(cur != group_next):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            recent_group_start = group_prev.next
            group_prev.next = kth
            group_prev = recent_group_start
