class Solution:
    def reverseWords(self, s: str) -> str:
        # s string
        # reverse order of the words
        s = s.strip()
        s_list = s.split()
        s_list.reverse()
        reversed_string = ' '.join(s_list)
        return reversed_string