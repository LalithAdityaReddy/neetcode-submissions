class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        n=len(nums)
        def helper(i,curr_sum):
            if i>=n:
                return 1 if curr_sum==target else 0
            if (i,curr_sum) in dp:
                return dp[(i,curr_sum)]
            add=helper(i+1,curr_sum+nums[i])
            sub=helper(i+1,curr_sum-nums[i])
            dp[(i,curr_sum)]=add+sub
            return dp[(i,curr_sum)]
        return helper(0,0)