class Node:
    def __init__(self, val: int, next_node: Node = None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        node = self.head
        while index > 0 and node is not None:
            node = node.next_node
            index -= 1
        if node is not None:
            return node.val
        return -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        tail = Node(val)
        if self.head is None:
            self.head = tail
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = tail

    def remove(self, index: int) -> bool:
        if self.head is None or index < 0:
            return False
        if index == 0:
            self.head = self.head.next_node
            return True
        last_node = self.head
        index -= 1
        node = self.head.next_node
        while index > 0 and node is not None:
            last_node = node
            node = node.next_node
            index -= 1
        if node is None:
            return False
        last_node.next_node = node.next_node
        return True

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        while node is not None:
            values.append(node.val)
            node = node.next_node
        return values        
