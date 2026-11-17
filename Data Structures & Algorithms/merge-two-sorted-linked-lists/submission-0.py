# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        merged_head = None
        while list1 is not None or list2 is not None:
            if list1 is None:
                if merged is None:
                    merged = list2
                    merged_head = list2
                else:
                    merged.next = list2
                    merged = list2
                list2 = None
            elif list2 is None:
                if merged is None:
                    merged = list1
                    merged_head = list1
                else:
                    merged.next = list1
                    merged = list1
                list1 = None
            elif list1.val <= list2.val:
                list1_next = list1.next
                list1.next = None
                if merged is None:
                    merged = list1
                    merged_head = list1
                else:
                    merged.next = list1
                    merged = list1
                list1 = list1_next
            else:
                list2_next = list2.next
                list2.next = None
                if merged is None:
                    merged = list2
                    merged_head = list2
                else:
                    merged.next = list2
                    merged = list2
                list2 = list2_next
        return merged_head