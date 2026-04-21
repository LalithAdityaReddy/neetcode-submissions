class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def func(idx,comb,t):
            if t<0 or idx==n:
                return
            if(t==0):
                ans.append(comb.copy())
                return
            comb.append(nums[idx])
            func(idx,comb,t-nums[idx])
            comb.pop()
            func(idx+1,comb,t)
            return
        func(0,[],target)
        return ans

        