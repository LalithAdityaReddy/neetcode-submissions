class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        ans=0
        prefixsum=0
        for i in nums:
            prefixsum+=i
            if prefixsum-k in d:
                ans+=d[prefixsum-k]
            d[prefixsum]=d.get(prefixsum,0)+1
        return ans