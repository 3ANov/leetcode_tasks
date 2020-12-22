#https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        if len(strs) == 0:
            return ''
        rsubstr = strs[0]
        rflag = True
        while len(rsubstr) > 0:
            for el in strs[1::]:
                if el.find(rsubstr) != 0:
                    rflag = False
                    break
            if rflag:
                return rsubstr
            rsubstr = rsubstr[:-1]
            rflag = True
        return ''


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
#print("abcd"[:-1])