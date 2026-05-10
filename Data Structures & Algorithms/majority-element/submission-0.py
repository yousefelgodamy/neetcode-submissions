class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length_nums_half = len(nums) // 2

        half = (length_nums_half // 2) + 1 if len(nums) % 2 == 1 else length_nums_half

        tracker = defaultdict(int)
        for x in nums:
            tracker[x] += 1
            if tracker[x] == half:
                return x
        
