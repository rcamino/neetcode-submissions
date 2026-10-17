class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = 0
        index = {}
        start = 0
        for i, c in enumerate(s):
            if c in index and index[c] >= start:
                longest = max(longest, count)
                start = index[c] + 1
                count = i - start + 1
                index[c] = i
            else:
                count += 1
                index[c] = i
        longest = max(longest, count)
        return longest