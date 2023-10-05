class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        i, j = 0, len(s_list) - 1

        while i < j:
            while i < j and s_list[i] not in vowels:
                i += 1
            while i < j and s_list[j] not in vowels:
                j -= 1

            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

        return ''.join(s_list)
