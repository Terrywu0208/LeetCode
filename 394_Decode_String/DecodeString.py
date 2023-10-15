class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack and stack[-1]!="[":
                    tmp = stack.pop()
                    substr = tmp + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    tmp = stack.pop()
                    k = tmp + k
                stack.append(int(k)*substr)
        return "".join(stack)