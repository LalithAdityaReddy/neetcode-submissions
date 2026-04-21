class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        curr=0
        for i in nums:
            curr+=i
            maxi=max(maxi,curr)
            if curr<0:
                curr=0
        return maxi