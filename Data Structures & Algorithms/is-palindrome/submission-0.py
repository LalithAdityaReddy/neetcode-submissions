import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=re.sub(r'[^a-zA-Z0-9]','',s)
        new=new.lower()
        if new==new[::-1]:
            return True
        return False
        

