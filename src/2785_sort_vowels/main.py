class Solution:
    def sortVowels(self, s: str) -> str:
        indices = []
        chars = []

        vowels = set('aeiouAEIOU')

        # Gather vowels
        for i, char in enumerate(s):
            if char in vowels:
                indices.append(i)
                chars.append(char)
                
        # Sort vowels
        chars.sort(key=ord)

        # Reinsert vowels
        strlist = list(s)
        for i, char in zip(indices, chars):
            strlist[i] = char
        return ''.join(strlist)

