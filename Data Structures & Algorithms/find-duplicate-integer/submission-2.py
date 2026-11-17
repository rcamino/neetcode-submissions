class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        other_slow = 0
        while slow != other_slow:
            other_slow = nums[other_slow]
            slow = nums[slow]
        return slow
