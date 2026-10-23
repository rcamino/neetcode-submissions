class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}
        for c in t:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        count = len(counter.keys())

        start = 0
        end = 0
        shortest = s
        found_at_least_once = False
        check_end = True
        print("counter:", counter)
        while start <= end and end < len(s):
            if check_end:
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

            found = count == 0
            if found:
                found_at_least_once = True
                length = end - start + 1
                if length < len(shortest):
                    shortest = s[start:end + 1]
                        
            if found or (not check_end and end == len(s) - 1):
                check_end = False
            else:
                end += 1
                check_end = True

        if found_at_least_once:
            return shortest
        return ""
