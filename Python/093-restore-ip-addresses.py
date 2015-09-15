#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-15 23:55:34
# Title      :  093 restore ip addresses

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if not s or len(s) > 12 or len(s) < 4:
            return result
        self.restore(s, 0, [], result)
        return result

    def restore(self, ip_str, idx, part, result):
        if idx >= len(ip_str):
            return
        if len(part) == 3:
            p = ip_str[idx:]
            if self.isValid(p):
                part.append(p)
                result.append('.'.join(part))
                return
        for i in range(1, 4):
            p = ip_str[idx:idx + i]
            if self.isValid(p):
                new_part = list(part)
                new_part.append(p)
                self.restore(ip_str, idx + i, new_part, result)

    def isValid(self, str):
        if not str or len(str) > 3:
            return False
        if str[0] == '0' and len(str) > 1:
            return False
        num = int(str)
        if 0 <= num <= 255:
            return True
        return False
