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
        closeToOpen = {')':'(','}':'{',']':'['}
        for i in s:
            #check if i is a closing string
            if i in closeToOpen:
                #check if stack is not empity
                #check if 'close' string matches with 'open' string
                if stack and closeToOpen[i] == stack[-1]:
                    stack.pop()
                ##check if i is a closing string and the stack is empity
                else:
                    return False
            #if i is not in closeToOpen, it's a open string
            else:
                stack.append(i)
        return True if not stack else False
    

sol = Solution()
rel = sol.isValid("()[]{}")
print('rel ', rel)