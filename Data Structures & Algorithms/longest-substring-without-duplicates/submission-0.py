class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        i=0
        cs=set()
        for j in range(len(s)):
            while s[j] in cs:
                cs.remove(s[i])
                i+=1
            cs.add(s[j])
            ans=max(ans,j-i+1)
        return ans