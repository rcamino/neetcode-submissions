class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = 0
        counter = {}
        for c in t:
            if c in counter:
                counter[c] += 1
            else:
                count += 1
                counter[c] = 1

        start = 0
        end = -1
        found = False
        shortest_start = 0
        shortest_end = -1
        shortest_length = len(s)
        while end == -1 or (start <= end and end < len(s)):
            if count > 0 and end < len(s) - 1:
                end += 1
                c = s[end]
                if c in counter:
                    counter[c] -= 1
                    if counter[c] == 0:
                        count -= 1
            else:
                c = s[start]
                if c in counter:
                    if counter[c] == 0:
                        count += 1
                    counter[c] += 1
                start += 1

            if count == 0:
                length = end - start + 1
                if not found or length < shortest_length:
                    shortest_start = start
                    shortest_end = end
                    shortest_length = length
                found = True

        if found:
            return s[shortest_start:shortest_end + 1]
        return ""
