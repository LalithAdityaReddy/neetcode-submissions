class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d={}
        def func(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if(j>=len(p)):
                return False
            valid=i<len(s) and (s[i]==p[j] or p[j]=='.')
            if(j+1<len(p) and p[j+1]=='*'):
                d[(i,j)]=func(i,j+2) or (valid and func(i+1,j))
                return d[(i,j)]
            if valid:
                d[(i,j)]=func(i+1,j+1)
                return d[(i,j)]
            else:
                d[(i,j)]=False
                return False
        return func(0,0)