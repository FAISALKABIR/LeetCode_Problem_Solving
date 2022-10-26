class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = 0
        carry = 0
        result = ""

        if len(a) > len(b):
            b = (len(a)-len(b)) * '0' + b
        else:
            a = (len(b)-len(a)) * '0' + a

        for i in range(len(a)-1, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            if (s == 1):
                s = 1
                carry = 0
            if (s == 2):
                s = 0
                carry = 1
            elif (s == 3):
                s = 1
                carry = 1
            result= str(s) + result 
            if i == 0 and carry == 1:
                result = str(carry) + result

        return result