class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in num_set:
                count = 1
                while len(nums) > count and num + count in num_set:
                    count += 1
                if count > longest:
                    longest = count
        return longest
