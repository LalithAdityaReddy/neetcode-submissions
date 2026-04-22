class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def func(s,comb):
            if len(s)==0:
                ans.append(comb.copy())
                return
            for i in range(len(s)):
                part=s[:i+1]
                if part==part[::-1]:
                    comb.append(part)
                    func(s[i+1:],comb)
                    comb.pop()
        func(s,[])
        return ans


