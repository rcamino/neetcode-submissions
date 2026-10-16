class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            if heights[left] < heights[right]:
                min_height = heights[left]
                new_left = left + 1
                new_right = right
            else:
                min_height = heights[right]
                new_left = left
                new_right = right - 1

            base = right - left
            area = base * min_height
            max_area = max(max_area, area)

            left = new_left
            right = new_right
        return max_area
