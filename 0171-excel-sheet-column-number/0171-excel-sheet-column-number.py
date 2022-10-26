class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        
        for i in columnTitle:
            value = ord(i) - ord('A') + 1
            output = 26 * output + value

        return output