from typing import List
from itertools import zip_longest


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        cn = groups[0]
        res = [words[0]]
        for word, group in zip(words[1:], groups[1:]):
            print(f"word={word}, group={group}, cn={cn}, res={res}, hamming_distance={self.hamming_distance(word, res[-1])}")
            if group != cn and self.hamming_distance(word, res[-1]) == 1:
                res.append(word)
                cn = group

        return res
    

    def hamming_distance(self, x: str, y: str) -> int:
        return sum(a != b for a, b in zip_longest(x, y, fillvalue=None))
        
if __name__ == "__main__":
    s = Solution()
    words = ["za","ay","aa","ba","bb","bc"]
    groups = [5,4,3,3,2,1]
    t1 = (words, groups)
    print(s.getWordsInLongestSubsequence(*t1))

