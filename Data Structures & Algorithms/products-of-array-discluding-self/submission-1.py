class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in range(len(nums))]
        i = 1
        while i < len(nums):
            left[i] = left[i - 1] * nums[i - 1]
            i += 1

        right = [1 for _ in range(len(nums))]
        i = len(nums) - 2
        while i >= 0:
            right[i] = right[i + 1] * nums[i + 1]
            i -= 1

        return [
            left[i] * right[i]
            for i in range(len(nums))
        ]