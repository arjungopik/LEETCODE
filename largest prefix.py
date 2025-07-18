# https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=""
        flag=1
        if len(strs)==1:
            return strs[0]
        for i in range(len(strs[0])):
            try:
                flag=1
                for val in strs:
                    if val[i]!=strs[0][i]:
                        flag = 0
                        break
                if flag == 1:
                    prefix+=strs[0][i]
                else:
                    return prefix
            except:
                return prefix

        return prefix
