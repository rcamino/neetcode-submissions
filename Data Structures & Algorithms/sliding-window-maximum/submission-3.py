import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        heap = []
        maxes = []
        for end in range(len(nums)):
            num = nums[end]
            if num in counts:
                counts[num] += 1
            else:
                heapq.heappush_max(heap, num)
                counts[num] = 1

            start = end - k + 1
            if start >= 0:
                if start > 0:
                    lost_num = nums[start - 1]
                    counts[lost_num] -= 1
                    if counts[lost_num] == 0:
                        counts.pop(lost_num)
                max_num = heap[0]
                while max_num not in counts and len(heap) > 0:
                    _ = heapq.heappop_max(heap)
                    max_num = heap[0]
                if max_num not in counts:
                    raise ValueError("Empty heap.")
                maxes.append(max_num)
        return maxes
