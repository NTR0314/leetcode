from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        cn = groups[0]
        res = [words[0]]
        for word, group in zip(words[1:], groups[1:]):
            if group != cn:
                res.append(word)
                cn = group

        return "".join(res)                
        
if __name__ == "__main__":
    s = Solution()
    t1 = (["e","a","b"], [0, 0, 1])
    t2 = (["a","b","c","d"], [1, 0, 1, 1])
    assert s.getLongestSubsequence(*t1) == "eb"
    assert s.getLongestSubsequence(*t2) == "abc"