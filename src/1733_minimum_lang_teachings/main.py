from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
    
        # Count problematic friendships
        problem_friendships = []

        # Might be useful to check for symmetry (2,3), (3,2)
        for f1, f2 in friendships:
            f1_langs = set(languages[f1-1])
            f2_langs = set(languages[f2-1])
            print(f1_langs, f2_langs)
            if f1_langs.isdisjoint(f2_langs):
                problem_friendships.append((f1, f2))

        # Find most common lang ?!?
        lang_freq = [0] * n
        
        users_checked = set()
        for problem_friendship in problem_friendships:
            f1 = problem_friendship[0]
            f2 = problem_friendship[1]
            f1_langs = set(languages[f1-1])
            f2_langs = set(languages[f2-1])
            
            for f in [f1, f2]:
                if f not in users_checked:
                    users_checked.add(f)
                    for lang in languages[f-1]:
                        lang_freq[lang-1] += 1
        
        # Get max index of lang_freq
        max_lang_index = 0
        max_lang_value = 0
        for i, freq in enumerate(lang_freq):
            if freq > max_lang_value:
                max_lang_value = freq
                max_lang_index = i

        # Teach lang_index to all not speaking users in problem friendships
        to_teach = 0
        users_taught = set()
        for problem_friendship in problem_friendships:
            f1 = problem_friendship[0]
            f2 = problem_friendship[1]
            f1_langs = set(languages[f1-1])
            f2_langs = set(languages[f2-1])
            
            for f in [f1, f2]:
                if f not in users_taught and (max_lang_index + 1) not in languages[f-1]:
                    users_taught.add(f)
                    to_teach += 1

        return to_teach

