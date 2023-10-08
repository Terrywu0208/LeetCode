class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        tmp = []
        while j < len(chars):
            if chars[i] == chars[j]:
                j += 1
            else:
                tmp.append(chars[i])
                if j - i > 1:
                    tmp.extend(list(str(j - i)))
                i = j
        tmp.append(chars[i])
        if j - i > 1:
            tmp.extend(list(str(j - i)))
        chars[:len(tmp)] = tmp
        return len(tmp)