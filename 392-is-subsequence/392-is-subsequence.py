class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sequence = t
    
        for char in s:
            ind = sequence.find(char)
            if ind == -1:
                return False
            else:
                sequence = sequence[ind + 1:]

        return True
            