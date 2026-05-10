class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_elements = 0
        to_add = []
        for i in range(len(nums)):
            if nums[i] != val:
                num_elements += 1
                to_add.append(nums[i])

        
        for j in range(len(to_add)):
            nums[j] = to_add[j]

        return num_elements
        