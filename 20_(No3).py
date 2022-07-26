class Solution:
    def isValid(self, s: str) -> bool:
        ss, sss, c, cc, x, xx, y = 0, 0, 0, 0, 0, 0, 0
        try :
            for i in s:
                xx = 0
                if x < 0:
                    return False
                if i == '(':
                    x += 3
                    sss = ss + 1
                    while s[sss] != ')' or y != 0:
                        if s[sss] == '(':
                            xx += 3
                            y += 1
                        elif s[sss] == '[':
                            xx += 5
                        elif s[sss] == '{':
                            xx += 7
                        elif s[sss] == ')':
                            xx -= 3
                            y -= 1
                        elif s[sss] == ']':
                            xx -= 5
                        elif s[sss] == '}':
                            xx -= 7
                        cc += 1
                        sss += 1
                    if xx != 0:
                        return False
                    cc = cc % 2
                    if cc == 1:
                        return False
                    ss += 1
                    c += 1
                elif i == '[':
                    x += 5
                    sss = ss + 1
                    while s[sss] != ']' or y != 0:
                        if s[sss] == '(':
                            xx += 3
                        elif s[sss] == '[':
                            xx += 5
                            y += 1
                        elif s[sss] == '{':
                            xx += 7
                        elif s[sss] == ')':
                            xx -= 3
                        elif s[sss] == ']':
                            xx -= 5
                            y -= 1 
                        elif s[sss] == '}':
                            xx -= 7
                        cc += 1
                        sss += 1
                    if xx != 0:
                        return False
                    cc = cc % 2
                    if cc == 1:
                        return False
                    ss += 1
                    c += 1
                elif i == '{':
                    x += 7
                    sss = ss + 1
                    while s[sss] != '}' or y != 0:
                        if s[sss] == '(':
                            xx += 3
                        elif s[sss] == '[':
                            xx += 5
                        elif s[sss] == '{':
                            xx += 7
                            y += 1
                        elif s[sss] == ')':
                            xx -= 3
                        elif s[sss] == ']':
                            xx -= 5
                        elif s[sss] == '}':
                            xx -= 7
                            y -= 1
                        cc += 1
                        sss += 1
                    if xx != 0:
                        return False
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
                
