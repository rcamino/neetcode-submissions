class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        start = 0
        for end in range(len(s2)):
            length = end - start + 1
            if length > len(s1):
                c = s2[start]
                start += 1
                if c in count:
                    count[c] += 1
                    if count[c] == 0:
                        count.pop(c)
                else:
                    count[c] = 1

            c = s2[end]
            if c in count:
                count[c] -= 1
                if count[c] == 0:
                    count.pop(c)
                    if len(count) == 0:
                        return True
            else:
                count[c] = -1
        return False