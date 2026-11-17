# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1_next = list1.next
            list1.next = None
            merged = list1
            list1 = list1_next
        else:
            list2_next = list2.next
            list2.next = None
            merged = list2
            list2 = list2_next

        merged_head = merged
        while list1 is not None or list2 is not None:
            if list1 is None:
                merged.next = list2
                merged = list2
                list2 = None
            elif list2 is None:
                merged.next = list1
                merged = list1
                list1 = None
            elif list1.val <= list2.val:
                list1_next = list1.next
                list1.next = None
                merged.next = list1
                merged = list1
                list1 = list1_next
            else:
                list2_next = list2.next
                list2.next = None
                merged.next = list2
                merged = list2
                list2 = list2_next
        return merged_head