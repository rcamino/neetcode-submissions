# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head_slow = head
        while head is not None and head.next is not None:
            head = head.next.next
            if head == head_slow:
                return True
            head_slow = head_slow.next
        return False
