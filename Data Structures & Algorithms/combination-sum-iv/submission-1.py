class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def helper(idx,s):
            if idx==len(nums):
                return 1 if s==target else 0
            if s>target:
                return 0
            if (idx,s) in dp:
                return dp[(idx,s)]
            t=helper(0,s+nums[idx])
            nt=helper(idx+1,s)
            dp[(idx,s)]=t+nt
            return dp[(idx,s)]
        dp={}
        return helper(0,0)

            