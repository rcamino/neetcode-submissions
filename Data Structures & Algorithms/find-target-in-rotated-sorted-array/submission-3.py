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
        original_length =  len(nums)
        start = rotated_start
        end = (rotated_start + original_length - 1) % original_length
        while True:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
        
            if end == start:
                return -1
            elif end > start:
                length = end - start + 1
                if length <= 2:
                    return -1
                mid = start + length // 2
            else:
                length = (end + 1) + (original_length - start)
                if length <= 2:
                    return -1
                mid = (start + length // 2) % original_length

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid