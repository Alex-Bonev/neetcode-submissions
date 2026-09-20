class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        translate = {')': '(', '}': '{', ']': '['}

        for item in s:
            if (item not in translate):
                stack.append(item)
            elif len(stack) > 0 and translate[item] == stack[-1]:
                stack.pop()
            else:
                return False
        return (len(stack) == 0)