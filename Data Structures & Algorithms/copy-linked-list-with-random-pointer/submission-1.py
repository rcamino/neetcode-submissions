# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        old_to_new = {}
        node = head
        while node is not None:
            new_node = Node(node.val)
            old_to_new[node] = new_node
            node = node.next

        node = head
        while node is not None:
            new_node = old_to_new[node]
            if node.next is not None:
                new_node.next = old_to_new[node.next]
            if node.random is not None:
                new_node.random = old_to_new[node.random]
            node = node.next

        return old_to_new[head]
