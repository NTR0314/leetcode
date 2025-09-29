class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_count = Solution.countVowels(s)
        
        # can't do anything
        if vowel_count == 0:
            return False

        # Delete whole thing
        elif vowel_count % 2 == 1:
            return True

        # Here I guess the optimal move is to delete everything except for one vowel
        # If there is only vowels left, then there is only one character left that Bob can not delete -> Alice wins
        # If there is other consonants left, bob can only delete the consonants, leaving one vowel for Alice -> Alice wins
        # I think the same holds if the vowel is sandwiched betwen consonants
        else:
            return True

    @staticmethod
    def countVowels(s:str) -> int:
        vowels = set('aeiouAEIOU')
        return sum(1 for char in s if char in vowels)
        