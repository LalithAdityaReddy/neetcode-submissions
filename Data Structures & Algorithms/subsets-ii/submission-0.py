class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def subsetstwo(idx,comb):
            if(idx>=len(nums)):
                ans.append(comb.copy())
                return         
            comb.append(nums[idx])
            subsetstwo(idx+1,comb)
            comb.pop()
            while(idx+1<len(nums) and nums[idx]==nums[idx+1]):
                idx+=1
            subsetstwo(idx+1,comb)   
        subsetstwo(0,[]) 
        return ans  