class Node:
    def __init__(self, val: int, next_node: Node = None):
        self.val = val
        self.next_node = next_node

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heads = {}
        nodes = {}
        for num in nums:
            if num not in nodes:
                if num + 1 in heads:
                    next_node = heads.pop(num + 1)
                    node = Node(num, next_node)
                else:
                    node = Node(num)

                nodes[num] = node

                if num - 1 in nodes:
                    prev_node = nodes[num - 1]
                    prev_node.next_node = node
                else:
                    heads[num] = node

        longest = 0
        for node in heads.values():
            length = 1
            node = node.next_node
            while node is not None:
                length += 1
                node = node.next_node
            if length > longest:
                longest = length
        return longest