# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: ListNode, k: int) -> tuple[ListNode, ListNode, ListNode]:
        i = 0
        node = head
        prev = None
        while node is not None and i < k:
            prev = node
            node = node.next
            i += 1
        if i < k:
            return head, prev, None

        i = 0
        node = head
        prev = None
        while node is not None and i < k:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            i += 1
        return prev, head, node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is not None:
            head, tail, remainder = self.reverse(head, k)

            while remainder is not None:
                new_head, new_tail, remainder = self.reverse(remainder, k)
                tail.next = new_head
                tail = new_tail
        return head
