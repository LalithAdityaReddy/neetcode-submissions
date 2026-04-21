class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return nums[i]
            d[nums[i]]=d.get(nums[i],0)+1
        