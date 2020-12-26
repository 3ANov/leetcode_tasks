class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_open_brackets = []
        s_list = [x for x in s]
        result = False
        try:
            for br in s_list:
                if br == '(' or br == '[' or br == '{':
                    list_open_brackets.append(br)
                else:
                    if list_open_brackets[-1] == '(' and br == ')':
                        list_open_brackets.pop()
                        result = True
                    elif list_open_brackets[-1] == '{' and br == '}':
                        list_open_brackets.pop()
                        result = True
                    elif list_open_brackets[-1] == '[' and br == ']':
                        list_open_brackets.pop()
                        result = True
                    else:
                        return False
        except IndexError:
            return False
        if list_open_brackets:
            return False
        return result









print(Solution().isValid(s="()"))