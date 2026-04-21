class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def perm(nums):
            i=len(nums)-2
            j=len(nums)-1
            while(i>=0 and nums[i]>=nums[i+1]):
                i-=1
            if i<0:
                return False
            while(nums[j]<=nums[i]):
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
            k=len(nums)-1
            l=i+1
            nums[i+1:]=reversed(nums[i+1:]) 
            return True
        ans=[nums[:]]
        while perm(nums):
            ans.append(nums[:])
        return ans          

