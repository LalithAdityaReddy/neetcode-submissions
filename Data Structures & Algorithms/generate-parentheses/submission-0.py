class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op=0
        cl=0
        def func(stack,op,cl):
            if op==cl==n:
                ans.append(''.join(stack))
                return
            if op<n:
                stack.append('(')
                func(stack,op+1,cl)
                stack.pop()
            if cl<op:
                stack.append(')')
                func(stack,op,cl+1)
                stack.pop()
        ans=[]
        func([],0,0)
        return ans