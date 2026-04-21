class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t)>len(s):
            return 0
        n=len(s)
        m=len(t)
        dp={}
        def func(i,temp):
            if i>=n:
                return 1 if temp==t else 0
            if(i,temp) in dp:
                return dp[(i,temp)]
            include=func(i+1,temp+s[i])
            exclude=func(i+1,temp)
            dp[(i,temp)]=include+exclude
            return dp[(i,temp)]
        return func(0,'')