class Solution:
    def reverseWords(self, s: str) -> str:
        original_list = s.split(" ")
        filtered_list = [item for item in original_list if item != '']
        i, j = 0, len(filtered_list)-1
        while i < j:
            filtered_list[i], filtered_list[j] = filtered_list[j], filtered_list[i]
            i+=1
            j-=1
        return " ".join(filtered_list)