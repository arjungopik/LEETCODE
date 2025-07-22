class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count =0
        for val in reversed(s):
            if val == " " and count >0:
                return count
            elif val != " ":
                count+=1
        return count