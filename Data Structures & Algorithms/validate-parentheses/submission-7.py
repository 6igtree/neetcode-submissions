class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in pairs:
                if len(stack) == 0:
                    return False
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        
        return stack == []


            