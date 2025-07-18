# https://leetcode.com/problems/roman-to-integer/submissions/1702695936/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        previouschr = 0
        for i in range(len(s)-1,-1,-1):
            currval = dict1[s[i]]
            if currval < previouschr:
                sum-=currval
            else:
                sum+=currval
            previouschr = currval
        return sum
        