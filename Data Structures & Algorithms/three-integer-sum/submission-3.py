class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for target, num_target in enumerate(nums):
            if len(triplets) > 0 and triplets[-1][0] == num_target:
                continue
            left = target + 1
            right = len(nums) - 1
            while left < right:
                num_left = nums[left]
                num_right = nums[right]
                if len(triplets) > 0 and triplets[-1] == (num_target, num_left, num_right):
                    left += 1
                    right -= 1
                elif num_left + num_right == - num_target:
                    triplets.append((num_target, num_left, num_right))
                    left += 1
                    right -= 1
                elif num_left + num_right < - num_target:
                    left += 1
                else:
                    right -= 1
        return triplets
