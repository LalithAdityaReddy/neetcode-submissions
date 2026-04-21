class Solution:
    def combinationSum4(self, nums, target):
        dp={}
        def helper(rem):
            if rem==0:
                return 1
            if rem<0:
                return 0
            if rem in dp:
                return dp[rem]
            ways=0
            for num in nums:
                ways+=helper(rem-num)
            dp[rem]=ways
            return ways
        return helper(target)