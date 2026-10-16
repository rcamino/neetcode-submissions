class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        for target, num_target in enumerate(nums):
            left = target + 1
            right = len(nums) - 1
            while left < right:
                num_left = nums[left]
                num_right = nums[right]
                if num_left + num_right == - num_target:
                    triplets.add((num_target, num_left, num_right))
                    left += 1
                    right -= 1
                elif num_left + num_right < - num_target:
                    left += 1
                else:
                    right -= 1
        return list(triplets)
