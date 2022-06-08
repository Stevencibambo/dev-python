class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for k, v in enumerate(nums):
            for n in range(k+1, len(nums)):
                if nums[n] + v == target and n != k:
                    return [k, n]