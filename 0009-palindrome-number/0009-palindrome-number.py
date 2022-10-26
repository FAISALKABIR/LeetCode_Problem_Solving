class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num = x
        
        while x > 0:
            temp = x % 10
            rev = rev * 10 + temp
            x //= 10
            
        if (num == rev):
            return True
        else:
            return False