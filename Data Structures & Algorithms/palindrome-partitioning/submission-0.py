class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def func(s,partitions):
            if len(s)==0:
                ans.append(partitions.copy())
                return
            for i in range(len(s)):
                part=s[:i+1]
                if part==part[::-1]:
                    partitions.append(part)
                    func(s[i+1:],partitions)
                    partitions.pop()
        func(s,[])
        return ans
