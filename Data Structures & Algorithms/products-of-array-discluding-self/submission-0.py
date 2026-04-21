class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        temp=[]
        for i in range(len(nums)):
            temp.append(prefix)
            prefix*=nums[i]
        postfix=1
        new=[]
        for i in range(len(nums)-1,-1,-1):
            temp[i]=temp[i]*postfix
            postfix*=nums[i]
        return temp

            