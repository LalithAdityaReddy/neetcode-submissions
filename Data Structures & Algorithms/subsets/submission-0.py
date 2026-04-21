class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def func(i,partitions):
            if i==len(nums):
                ans.append(partitions.copy())
                return
            partitions.append(nums[i])
            include=func(i+1,partitions)
            partitions.pop()
            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            exclude=func(i+1,partitions)
            return
        func(0,[])
        return ans
