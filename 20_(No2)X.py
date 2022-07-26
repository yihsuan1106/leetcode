class Solution:
    def isValid(self, s: str) -> bool:
        ss, sss, c, cc, x = 0, 0, 0, 0, 0
        try :
            for i in s:
                if x < 0:
                    return False
                if i == '(':
                    x += 3
                    sss = ss + 1
                    while s[sss] != ')':
                        cc += 1
                        sss += 1
                    cc = cc % 2
                    if cc == 1:
                        return False
                    ss += 1
                    c += 1
                elif i == '[':
                    x += 5
                    sss = ss + 1
                    while s[sss] != ']':
                        cc += 1
                        sss += 1
                    cc = cc % 2
                    if cc == 1:
                        return False
                    ss += 1
                    c += 1
                elif i == '{':
                    x += 7
                    sss = ss + 1
                    while s[sss] != '}':
                        cc += 1
                        sss += 1
                    cc = cc % 2
                    if cc == 1:
                        return False
                    ss += 1
                    c += 1
                elif i == ')':
                    x -= 3
                    ss += 1
                    c += 1
                elif i == ']':
                    x -= 5
                    ss += 1
                    c += 1
                elif i == '}':
                    x -= 7
                    ss += 1
                    c += 1
        except:
            return False
        if c % 2 == 0:
            return True
        else:
            return False
                
