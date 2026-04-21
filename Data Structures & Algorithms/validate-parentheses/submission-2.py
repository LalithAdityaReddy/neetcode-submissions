class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if not stack:
                    return False
                e=stack.pop()
                if(i==')' and e!='(') or (i==']' and e!='[') or (i=='}' and e!='{'):
                    return False
        return True if not stack else False

