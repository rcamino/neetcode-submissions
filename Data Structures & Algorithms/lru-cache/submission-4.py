class Node:
    def __init__(self, key: int):
        self.key = key
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return repr(self.key)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = {}
        self.key_node = {}
        self.head = None
        self.tail = None

    def _use(self, key: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            if self.head != node:
                prev_node = node.prev_node
                next_node = node.next_node
                if node == self.tail:
                    self.tail = prev_node
                if prev_node is not None:
                    prev_node.next_node = next_node
                if next_node is not None:
                    next_node.prev_node = prev_node
                self.head.prev_node = node
                node.prev_node = None
                node.next_node = self.head
                self.head = node
        else:
            node = Node(key)
            self.key_node[key] = node

            if self.head is not None:
                self.head.prev_node = node
                node.next_node = self.head
            self.head = node
            
            if self.tail is None:
                self.tail = node

    def get(self, key: int) -> int:
        if key in self.key_value:
            self._use(key)
            return self.key_value[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.key_value[key] = value
        self._use(key)
        if len(self.key_value) > self.capacity:
            lru_node = self.tail
            self.tail = lru_node.prev_node
            lru_node.prev_node = None
            self.key_value.pop(lru_node.key)
            self.key_node.pop(lru_node.key)
