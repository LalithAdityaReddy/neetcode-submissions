class Solution:
    def isFreqSame(self,freq: str,windowFreq:str)->bool:
        for i in range(26):
            if(freq[i]!=windowFreq[i]):
                return False
        return True        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq=[0]*26
        for i in range(len(s1)):
            freq[ord(s1[i])-ord('a')]+=1
        windowSize=len(s1)
        for i in range(len(s2)):
            windowFreq=[0]*26
            windIdx=0
            idx=i
            while(windIdx<windowSize and idx<len(s2)):
                windowFreq[ord(s2[idx])-ord('a')]+=1
                windIdx+=1
                idx+=1
            if(self.isFreqSame(freq,windowFreq)):
                return True
        return False        

