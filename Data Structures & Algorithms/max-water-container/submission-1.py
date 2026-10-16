class Solution:
    def area(self, heights: List[int], left: int, right: int) -> int:
        base = right - left
        min_height = min(heights[left], heights[right])
        return base * min_height

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            area = self.area(heights, left, right)
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
