class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            if start == end:
                mid = start
            else:
                mid = start + (end - start + 1) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
