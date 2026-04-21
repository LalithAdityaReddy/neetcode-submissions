class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        d={}
        def func(i,j):
            if j-i<=1:
                return 0
            if (i,j) in d:
                return d[(i,j)]
            ans=0
            for k in range(i+1,j):
                val=nums[i]*nums[k]*nums[j]
                val+=func(i,k)+func(k,j)
                ans=max(ans,val)
            d[(i,j)]=ans
            return d[(i,j)]
        return func(0,n-1)
            