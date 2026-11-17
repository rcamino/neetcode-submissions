from math import ceil
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        count = 0
        node = head
        while node is not None:
            count += 1
            node = node.next

        if count < 2:
            return
            
        count_forward = ceil(count / 2)
        i = 1
        node = head
        while i < count_forward:
            i += 1
            node = node.next

        last_forward = node
        prev = last_forward.next
        node = prev.next
        prev.next = None
        while node is not None:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        tail = prev

        node = head
        while node is not None:
            node_next = node.next
            if node == head:
                node.next = tail
                head = node_next
            else:
                node.next = head
                tail = node_next
            node = node.next
