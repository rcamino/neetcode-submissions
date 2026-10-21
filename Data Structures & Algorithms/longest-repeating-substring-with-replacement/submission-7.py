from collections import Counter

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        best = 1
        c = s[0]
        counter = Counter({c: 1})
        start = 0
        bad = 0
        length = 1
        for end in range(1, len(s)):
            c = s[end]
            counter += Counter({c : 1})
            chosen, good = counter.most_common(n=1)[0]
            length = end - start + 1
            bad = length - good
            if bad > k:
                best = max(best, length - 1)
                c_start = s[start]
                counter -= Counter({c_start : 1})
                start += 1
        if bad <= k:
            best = max(best, length)
        return best