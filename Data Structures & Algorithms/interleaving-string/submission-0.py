class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s1)
        m=len(s2)
        dp={}
        def func(i,j,k):
            if(k==len(s3)):
                return i==n and j==m
            if(i,j) in dp:
                return dp[(i,j)]
            ans=False
            if(i<len(s1) and s1[i]==s3[k]):
                ans=ans or func(i+1,j,k+1)
            if(j<len(s2) and s2[j]==s3[k]):
                ans=ans or func(i,j+1,k+1)
            dp[(i,j)]=ans
            return dp[(i,j)]
        return func(0,0,0)