class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        rules=['*','/','+','-']
        for i in tokens:
            if(i not in rules):
                stack.append(int(i))
            else:
                n1=stack.pop()
                n2=stack.pop()
                if i=='*':
                    stack.append(n2*n1)
                elif i=='/':
                    stack.append(int(n2/n1))
                elif i=='+':
                    stack.append(n2+n1)
                else:
                    stack.append(n2-n1)
        return stack[0]