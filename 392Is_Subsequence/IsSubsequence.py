class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        t_i = 0
        tmp = []
        while t_i < len(t) and s_i < len(s):
            if s[s_i] == t[t_i]:
                tmp.append(s[s_i])
                s_i+=1
                t_i+=1
            else:
                t_i+=1
        return "".join(tmp) == s
