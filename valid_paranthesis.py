class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in (')', '}', ']'):
                if len(stack) < 1:
                    return False
                elif stack[-1] == '(' and i != ')':
                    return False
                elif stack[-1] == '{' and i != '}':
                    return False    
                elif stack[-1] == '[' and i != ']':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
        
