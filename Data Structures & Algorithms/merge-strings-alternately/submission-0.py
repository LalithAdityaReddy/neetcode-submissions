class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=0
        l2=0
        s=''
        while(l1<len(word1) and l2<len(word2)):
            s+=word1[l1]
            s+=word2[l2]
            l1+=1
            l2+=1
        while(l1<len(word1)):
            s+=word1[l1]
            l1+=1
        while(l2<len(word2)):
            s+=word2[l2]
            l2+=1
        return s
        