class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'ABC',
        '3':'DEF',
        '4':'GHI',
        '5':'JKL',
        '6':'MNO',
        '7':'PQRS',
        '8':'TUV',
        '9':'WXYZ'
        }
        n=len(digits)
        ans=[]
        def func(i,comb):
            if len(comb)==n:
                ans.append(comb)
                return 
            for k in d[digits[i]]:
                func(i+1,comb+k.lower())
        if digits:
            func(0,'')
        return ans


            