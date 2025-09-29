from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result = []
        
        word_set = set(wordlist)
        vowels = set('aeiouAEIOU')
        normalized_words = {word.lower(): word for word in reversed(wordlist)}
        non_vower_words = {''.join(['*' if c in vowels else c for c in word.lower()]):word for word in reversed(wordlist)}
        
        for query in queries:
            print(f"\nQUERY: {query}")
            
            # 1. Exact match
            if query in word_set:
                result.append(query)
                continue
            
            matched = False
            # 2. Case-insensitive match
            if query.lower() in normalized_words:
                result.append(normalized_words[query.lower()])
                continue
            
            # 3. Vowel error match
            if (nvw := ''.join(['*' if c in vowels else c for c in query.lower()])) in non_vower_words:
                result.append(non_vower_words[nvw])
                continue
            
            result.append("")
        
        return result
