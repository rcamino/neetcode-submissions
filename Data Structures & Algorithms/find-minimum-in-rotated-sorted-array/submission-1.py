class Solution:
    def previousIndex(self, i: int, nums: List[int]) -> int:
        return i - 1 if i > 0 else len(nums) - 1

    def isMin(self, i: int, nums: List[int]) -> bool:
        i_prev = self.previousIndex(i, nums)
        i_prev_prev = self.previousIndex(i_prev, nums)
        return nums[i] < nums[i_prev] and nums[i_prev] > nums[i_prev_prev]

    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        start = 0
        end = len(nums) - 1
        while start <= end:
            if self.isMin(start, nums):
                return nums[start]
            if self.isMin(end, nums):
                return nums[end]

            mid = start + (end - start + 1) // 2
            if self.isMin(mid, nums):
                return nums[mid]
            elif nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        raise ValueError("OH NO")
