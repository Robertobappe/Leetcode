from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        '''
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif len(stack) > 0 and stack[-1] == '(' and i == ')' or len(stack) > 0 and stack[-1] == '[' and i == ']' or len(stack) > 0 and stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False'''

        #Another solution
        mapC = {')':'(','}':'{',']':'['}
        for i in s:
            if mapC[i]:
                stack.pop()
            stack.append(i)
        if len(stack) == 0:
            return True
        return False

    

sol = Solution()
rel = sol.isValid("()")
print('rel ', rel)