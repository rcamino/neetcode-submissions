# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        node = head
        while node is not None:
            sz += 1
            node = node.next

        if sz == n:
            return head.next

        m = sz
        prev = None
        node = head
        while m > n:
            m -= 1
            prev = node
            node = node.next
        prev.next = node.next
        node.next = None
        return head