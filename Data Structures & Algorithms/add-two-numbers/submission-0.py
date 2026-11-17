# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3_head = None
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                val = l2.val
                l2 = l2.next
            elif l2 is None:
                val = l1.val
                l1 = l1.next
            else:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            
            val += carry
            if val > 9:
                carry = 1
                val -= 10
            else:
                carry = 0

            if l3_head is None:
                l3_head = ListNode(val)
                l3 = l3_head
            else:
                l3.next = ListNode(val)
                l3 = l3.next

        if carry > 0:
            l3.next = ListNode(carry)
        return l3_head
