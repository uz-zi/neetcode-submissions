"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None:None}
        node = head
        while node:
            copy = Node(node.val)
            dic[node] = copy
            node = node.next
        
        node = head
        while node:
            copy = dic[node]
            copy.next = dic[node.next]
            copy.random = dic[node.random]
            node = node.next

        return dic[head]



        