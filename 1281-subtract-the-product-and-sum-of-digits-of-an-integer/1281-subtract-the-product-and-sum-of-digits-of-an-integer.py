class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        
        for digit in str(n):
            prod *= int(digit)
            sum += int(digit)
            
        return (prod - sum)