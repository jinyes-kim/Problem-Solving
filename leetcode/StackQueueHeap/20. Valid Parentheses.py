class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
                   
        for ch in s:
            if ch not in table:
                stack.append(ch)
            
            elif not stack or table[ch] != stack.pop():
                return False
        
        if len(stack) == 0:
            return True
        return False
        