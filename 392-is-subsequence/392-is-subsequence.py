class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sequence = t
    
        for char in s:
            str_index = sequence.find(char)
            if str_index == -1:
                return False
            else:
                sequence = sequence[str_index + 1:]

        return True