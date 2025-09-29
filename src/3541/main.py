import collections

class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = collections.Counter(s)
        
        vowels = set('aeiou')

        max_vowel_freq = max((counts[v] for v in vowels if v in counts), default=0)

        max_consonant_freq = max((freq for char, freq in counts.items() if char not in vowels), default=0)
        
        return max_vowel_freq + max_consonant_freq