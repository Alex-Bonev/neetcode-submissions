class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = {'(', '{', '['}
        
        translate = {')': '(', '}': '{', ']': '['}

        for item in s:
            if (item in o):
                stack.append(item)
            elif len(stack) > 0 and translate[item] == stack[-1]:
                stack.pop()
            else:
                return False
        return (len(stack) == 0)