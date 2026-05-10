class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = defaultdict(lambda: -1) # diff -> index
        for i in range(len(nums)):
            diff = target - nums[i]

            prev_diff_index = diffs[diff]
            if prev_diff_index >= 0:
                return [prev_diff_index, i]
            else:
                diffs[nums[i]] = i