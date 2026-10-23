from sortedcontainers import SortedDict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        sorted_counts = SortedDict()
        for end in range(len(nums)):
            num = nums[end]
            if num in sorted_counts:
                sorted_counts[num] += 1
            else:
                sorted_counts[num] = 1

            start = end - k + 1
            if start >= 0:
                if start > 0:
                    lost_num = nums[start - 1]
                    sorted_counts[lost_num] -= 1
                    if sorted_counts[lost_num] == 0:
                        del sorted_counts[lost_num]
                maxes.append(sorted_counts.peekitem(-1)[0])
        return maxes
