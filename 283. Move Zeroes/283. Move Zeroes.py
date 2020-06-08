class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct = 0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                nums[ct],nums[i] = nums[i],nums[ct]
                ct += 1



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(min(strs,key=lambda x: len(x))):