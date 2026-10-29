class TimeMap:

    def __init__(self):
        self.entries_by_key = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.entries_by_key:
            self.entries_by_key[key] = []
        self.entries_by_key[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.entries_by_key:
            return ""
        entries = self.entries_by_key[key]

        first = 0
        first_timestamp, first_value = entries[first]
        if timestamp < first_timestamp:
            return ""

        last = len(entries) - 1
        last_timestamp, last_value = entries[last]

        while first <= last:
            if timestamp >= last_timestamp:
                return last_value      
            if timestamp == first_timestamp or last - first == 1:
                return first_value

            mid = first + (last - first) // 2
            mid_timestamp, mid_value = entries[mid]
            if timestamp <= mid_timestamp:
                last = mid
                last_timestamp = mid_timestamp
                last_value = mid_value
            else:
                first = mid
                first_timestamp = mid_timestamp
                first_value = mid_value
        return ""
