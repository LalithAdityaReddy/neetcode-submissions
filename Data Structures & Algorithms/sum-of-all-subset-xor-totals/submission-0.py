class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans=0
        def helper(idx,comb):
            if idx>=len(nums):
                cn=0
                for i in comb:
                    cn^=i
                self.ans+=cn
                return 
            comb.append(nums[idx])
            helper(idx+1,comb)
            comb.pop()
            helper(idx+1,comb)
            return 
        helper(0,[])
        return self.ans