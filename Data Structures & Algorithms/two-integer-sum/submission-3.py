class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_indexes = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in num_to_indexes:
                num_to_indexes[num] = []
            num_to_indexes[num].append(i)

        for i in range(len(nums)):
            num_i = nums[i]
            num_j = target - num_i
            if num_j in num_to_indexes:
                indexes = num_to_indexes[num_j]
                if i != indexes[0]:
                    return [i, indexes[0]]
                elif len(indexes) > 1:
                    return [i, indexes[1]]
