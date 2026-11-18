# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_head = None
        merged_node = None
        heap = []
        tiebreaker = 0
        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, tiebreaker, node))
                tiebreaker += 1

        while len(heap) > 0:
            val, _, node = heapq.heappop(heap)
            next_node = node.next
            if next_node is not None:
                heapq.heappush(heap, (next_node.val, tiebreaker, next_node))
                tiebreaker += 1
            node.next = None
            if merged_head is None:
                merged_head = node
            else:
                merged_node.next = node
            merged_node = node

        return merged_head
