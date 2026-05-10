class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_elements = 0
        to_remove = []
        for i in range(len(nums)):
            if nums[i] != val:
                num_elements += 1
            else:
                to_remove.append(i)

        to_remove.reverse()
        for j in to_remove:
            nums.pop(j)

        return num_elements
        