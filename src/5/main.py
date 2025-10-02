from functools import cache


class Solution:
    def longestPalindrome(self, s: str):
        @cache
        def is_palindrome(i: int, j: int) -> bool:
            # Base case: an empty or single-character string is a palindrome
            if i >= j:
                return True
            
            # Recursive step: check if the ends match and the inside is also a palindrome
            return s[i] == s[j] and is_palindrome(i + 1, j - 1)

        bl = 0
        cb = s[0]

        for l in range(0, len(s)):
            for r in range(0, len(s)):
                if r - l < 1:
                    continue
                if s[l] == s[r]:
                    if is_palindrome(l, r):
                        if r - l + 1 > bl:
                            bl = r - l + 1
                            cb = s[l : r + 1]
        return cb


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ac"))
    print(s.longestPalindrome("ccc"))
    print(s.longestPalindrome("aacabdkacaa"))
