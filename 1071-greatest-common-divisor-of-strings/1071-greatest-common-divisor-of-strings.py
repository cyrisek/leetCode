class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        len1, len2 = len(str1), len(str2)
        length = self.gcd(len1, len2)

        if str1 + str2 != str2 + str1:
            return ""

        divisor = str1[:length]

        if divisor * (len1 // length) == str1 and divisor * (len2 // length) == str2:
            return divisor
        else:
            return ""

    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)