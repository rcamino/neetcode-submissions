class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.elements = [0 for _ in range(capacity)]


    def get(self, i: int) -> int:
        return self.elements[i]

    def set(self, i: int, n: int) -> None:
        self.elements[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.elements[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.elements[self.size]

    def resize(self) -> None:
        old_capacity = self.capacity
        self.capacity = old_capacity * 2
        self.elements = [
            self.elements[i] if i < old_capacity else 0
            for i in range(self.capacity)
        ]

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
