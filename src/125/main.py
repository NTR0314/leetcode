class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        legal = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

        while l < r:
            if s[l] not in legal:
                l += 1
                continue
            if s[r] not in legal:
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                continue
            else:
                return False
        return True