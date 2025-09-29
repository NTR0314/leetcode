from itertools import combinations
from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0.
        combs = combinations(points, r=3)
        for comb in combs:
            x1, y1 = comb[0]
            x2, y2 = comb[1]
            x3, y3 = comb[2]
            area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
            res = max(res, area)
        
        return res