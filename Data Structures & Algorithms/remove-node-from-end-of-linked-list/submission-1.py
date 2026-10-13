class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        # move fast n+1 steps
        for i in range(n + 1):
            fast = fast.next

        # move both
        while fast:
            slow = slow.next
            fast = fast.next

        # delete node
        slow.next = slow.next.next

        return dummy.next