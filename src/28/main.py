class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        i = 0
        j = 0

        fl = 0
        while i < len(haystack):
            if needle[j] == haystack[i+j]:
                j += 1
                fl += 1
                if fl == len(needle) - 1:
                    return i
                continue
            else:
                fl = 0
                j = 0
                i += 1

        return -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.strStr("mississippi", "issipi"))  # Output: 4