class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        last_index = {}
        for i, num in enumerate(nums):
            last_index[num] = i

        triplets = set()
        for i, num_i in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num_j = nums[j]
                num_k = - (num_i + num_j)
                if num_k in last_index:
                    k = last_index[num_k]
                    if i < k and j < k:
                        triplet = tuple(sorted([num_i, num_j, num_k]))
                        triplets.add(triplet)
        return list(triplets)
