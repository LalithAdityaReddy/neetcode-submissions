class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        resLen=0
        for i in range(len(s)):
            j=i
            k=j
            while(j>=0 and k<len(s) and s[j]==s[k]):
                if k-j+1>resLen:
                    resLen=k-j+1
                    res=s[j:k+1]
                j-=1
                k+=1
        for i in range(len(s)):
            j=i
            k=j+1
            while(j>=0 and k<len(s) and s[j]==s[k]):
                if k-j+1>resLen:
                    resLen=k-j+1
                    res=s[j:k+1]
                j-=1
                k+=1
        return res