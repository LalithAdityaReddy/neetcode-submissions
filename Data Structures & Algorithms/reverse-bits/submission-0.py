class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)
        b=b[2:]
        b1=b[::-1]
        while(len(b1)<32):
            b1+='0'
        return int(b1,2)