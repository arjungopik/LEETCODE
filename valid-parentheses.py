# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict1 = {'}':'{',']':'[',')':"("} 
        stack = []
        for val in s:
            try:
                if val in dict1.values():
                    stack.append(val)
                elif stack[-1] == dict1[val]:
                        stack.pop()
                else:
                    return False
            except:
                return False
        if len(stack)==0:
            return bool(1)
        else: 
            return bool(0)


        