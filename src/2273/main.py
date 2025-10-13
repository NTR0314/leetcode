from typing import List
from collections import Counter
from itertools import groupby


# class Solution:
#     def removeAnagrams(self, words: List[str]) -> List[str]:
#         res = [words[0]]
#         prev = Counter(words[0])
#         for word in words[1:]:
#             cur = Counter(word)
#             if prev == cur:
#                 continue
#             else:
#                 res.append(word)
#                 prev = cur
#         return res

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [next(g) for _, g in groupby(words, sorted)]
    
if __name__ == "__main__":
    s = Solution()
    print(s.removeAnagrams(words = ["a", "b", "a"]))