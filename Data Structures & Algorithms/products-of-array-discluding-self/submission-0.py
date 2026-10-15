class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        has_zero = False
        for num in nums:
            if num == 0 and has_zero:
                all_product = 0
            elif num == 0:
                has_zero = True
            else:
                all_product = all_product * num
        return [
            int(all_product / num) if not has_zero else (all_product if num == 0 else 0)
            for num in nums
        ]