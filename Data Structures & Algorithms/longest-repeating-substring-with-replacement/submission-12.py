class Solution:
    A = ord("A")
    Z = ord("Z")

    def characterReplacement(self, s: str, k: int) -> int:
        best = 1
        counter = [0 for _ in range(self.Z - self.A + 1)]
        c = s[0]
        i = ord(c) - self.A
        counter[i] += 1
        start = 0
        bad = 0
        length = 1
        for end in range(1, len(s)):
            c = s[end]
            i = ord(c) - self.A
            counter[i] += 1
            good = max(counter)
            length = end - start + 1
            bad = length - good
            if bad > k:
                best = max(best, length - 1)
                c = s[start]
                i = ord(c) - self.A
                counter[i] -= 1
                start += 1
        if bad <= k:
            best = max(best, length)
        return best