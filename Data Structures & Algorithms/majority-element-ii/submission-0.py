class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        ans=[]
        for key,val in d.items():
            if val>n//3:
                ans.append(key)
        return ans