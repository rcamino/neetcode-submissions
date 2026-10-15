class Node:
    def __init__(self, val: int, next_node: Node = None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
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
        self.size += 1

    def insertTail(self, val: int) -> None:
        tail = Node(val)
        if self.head is None:
            self.head = tail
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = tail
        self.size += 1

    def remove(self, index: int) -> bool:
        if self.head is None or index < 0:
            return False
        if index == 0:
            self.head = self.head.next_node
            self.size -= 1
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
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = [None for _ in range(self.size)]
        i = 0
        node = self.head
        while node is not None:
            values[i] = node.val
            i += 1
            node = node.next_node
        return values        
