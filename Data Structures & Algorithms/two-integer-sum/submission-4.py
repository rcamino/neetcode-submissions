class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_first_index = {}
        num_to_second_index = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in num_to_first_index:
                num_to_first_index[num] = i
            elif num not in num_to_second_index:
                num_to_second_index[num] = i

        for i in range(len(nums)):
            num_i = nums[i]
            num_j = target - num_i
            if num_j in num_to_first_index:
                j = num_to_first_index[num_j]
                if i != j:
                    return [i, j]
                elif num_j in num_to_second_index:
                    j = num_to_second_index[num_j]
                    return [i, j]
