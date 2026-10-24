class Solution:
    def previousIndex(self, i: int, nums: List[int]) -> int:
        return i - 1 if i > 0 else len(nums) - 1

    def isMin(self, i: int, nums: List[int]) -> bool:
        i_prev = self.previousIndex(i, nums)
        i_prev_prev = self.previousIndex(i_prev, nums)
        return nums[i] < nums[i_prev] and nums[i_prev] > nums[i_prev_prev]

    def findRotatedStart(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] < nums[1] else 1
        start = 0
        end = len(nums) - 1
        while True:
            if self.isMin(start, nums):
                return start
            if self.isMin(end, nums):
                return end

            mid = start + (end - start + 1) // 2
            if self.isMin(mid, nums):
                return mid
            elif nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1

    def rotatedIndex(self, i: int, start: int, length: int) -> int:
        return (start + i) % length

    def search(self, nums: List[int], target: int) -> int:
        rotated_start = self.findRotatedStart(nums)
        if rotated_start == 0:
            start = 0
            end = len(nums) - 1
        elif target < nums[0]:
            start = rotated_start
            end = len(nums) - 1
        else:
            start = 0
            end = rotated_start - 1

        while start <= end:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            if start == end:
                break
            
            length = end - start + 1
            mid = start + length // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1