class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        def func(idx,comb,t):
            if(t==target):
                ans.append(comb.copy())
                return
            if t>target or idx==n:
                return
            comb.append(nums[idx])
            func(idx+1,comb,t+nums[idx])
            comb.pop()
            while(idx+1<n and nums[idx]==nums[idx+1]):
                idx+=1
            func(idx+1,comb,t)
            return
        func(0,[],0)
        return ans