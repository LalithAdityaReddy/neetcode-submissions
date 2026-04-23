class Solution:
    def reverse(self, x: int) -> int:
        def func(val):
            l=[]
            while val!=0:
                l.append(val%10)
                val=val//10
            return l
        arr=func(abs(x))
        n=len(arr)
        val=10**(n-1)
        ans=0
        for i in arr:
            ans+=i*val
            val=val//10
        if x>0 and ans in range(-2**31,2**31):
            return ans
        elif x<0 and ans in range(-2**31,2**31):
            return -ans
        else:
            return 0
