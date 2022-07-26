class Solution:
    def isValid(self, s: str) -> bool:
        x = 0 #()-> 3, []-> 5, {}-> 7
        c = ''
        for i in s:
            if x < 0:
                return False
            if i == '(':
                x += 3
                c = '('
            elif i == '[':
                x += 5
                c = '['
            elif i == '{':
                x += 7
                c = '{'
            elif i == ')':
                x -= 3
                if c == '{' or c == '[' :
                    return False
                c = ''
            elif i == ']':
                x -= 5
                if c == '(' or c == '{' :
                    return False
                c = ''
            elif i == '}':
                x -= 7
                if c == '(' or c == '[' :
                    return False
                c = ''
        if x == 0:
            return True
        else:
            return False
