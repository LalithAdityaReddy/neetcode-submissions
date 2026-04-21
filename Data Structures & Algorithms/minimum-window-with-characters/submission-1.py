class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        d_t={}
        d_s={}
        if len(t)>len(s):
            return ""
        if any(ch not in s for ch in t):
            return ""
        for i in t:
            d_t[i]=d_t.get(i,0)+1
        def isvalid():
            for i in d_t:
                if d_s.get(i,0)<d_t[i]:
                    return False
            return True
        ans=float('inf')
        f=""
        for i in range(len(s)):
            d_s[s[i]]=d_s.get(s[i],0)+1
            while isvalid():
                if i-left+1<ans:
                    ans=i-left+1
                    f=s[left:i+1]
                d_s[s[left]]-=1
                if d_s[s[left]]==0:
                    del d_s[s[left]]
                left+=1
        return f
        