from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.key_value = {}
        self.key_time = {}
        self.capacity = capacity
        self.t = 0

    def get(self, key: int) -> int:
        if key in self.key_value:
            self.t += 1
            self.key_time[key] = self.t
            return self.key_value[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.t += 1
        self.key_value[key] = value
        self.key_time[key] = self.t
        if len(self.key_value) > self.capacity:
            min_t = self.t
            for other_key, other_t in self.key_time.items():
                if other_t < min_t:
                    min_t = other_t
                    min_key = other_key
            self.key_value.pop(min_key)
            self.key_time.pop(min_key)
