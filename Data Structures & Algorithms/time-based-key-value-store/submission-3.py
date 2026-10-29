class TimeMap:

    def __init__(self):
        self.entries_by_key = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.entries_by_key:
            self.entries_by_key[key] = []
        self.entries_by_key[key].append({
            "timestamp": timestamp,
            "value": value,
        })

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.entries_by_key:
            return ""
        entries = self.entries_by_key[key]

        first = 0
        first_entry = entries[first]
        if timestamp < first_entry["timestamp"]:
            return ""

        last = len(entries) - 1
        last_entry = entries[last]
        
        while first <= last:
            if timestamp >= last_entry["timestamp"]:
                return last_entry["value"]            
            if timestamp == first_entry["timestamp"] or last - first == 1:
                return first_entry["value"]

            mid = first + (last - first) // 2
            mid_entry = entries[mid]
            if timestamp <= mid_entry["timestamp"]:
                last = mid
                last_entry = entries[last]
            else:
                first = mid
                first_entry = entries[first]
        return ""
