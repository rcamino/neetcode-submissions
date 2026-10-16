class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i - 1])

        suffix = [0 for _ in range(len(height))]
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])

        min_height = [min(prefix[i], suffix[i]) for i in range(len(height))]

        accumulated = 0
        for i in range(len(height)):
            if min_height[i] > height[i]:
                accumulated += min_height[i] - height[i]
        return accumulated
