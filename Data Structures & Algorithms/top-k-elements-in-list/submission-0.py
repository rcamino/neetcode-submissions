class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        tuples = list(counter.items())
        tuples = sorted(tuples, key=lambda t: t[1], reverse=True)
        return [tuples[i][0] for i in range(k)]
