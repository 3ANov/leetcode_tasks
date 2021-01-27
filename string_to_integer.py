class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            sign = 1
            digit_str = s.strip().split()[0]
            if digit_str[0] == '-':
                sign = -1
                digit_str = digit_str[1:]
            elif digit_str[0] == '+':
                sign = 1
                digit_str = digit_str[1:]
            list_digit_str = list(digit_str)
            if not list_digit_str:
                return 0
            if not list_digit_str[0].isdigit():
                return 0
            new_digit_str = ''
            for ch in list_digit_str:
                if ch.isdigit():
                    new_digit_str += ch
                else:
                    break
            digit = sign*int(new_digit_str)
            return digit if -2 ** 31 <= digit <= 2 ** 31 - 1 else -2147483648 if digit < 0 else 2147483647
        except IndexError:
            return 0


str = " +5"
print(Solution().myAtoi(str))
