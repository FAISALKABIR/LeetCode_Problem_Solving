class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        index_s = 0
        index_t = 0
        
        while index_s < len_s and index_t < len_t:
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1
            
        if index_s == len_s:
            return True
        else:
            return False
            