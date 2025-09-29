from typing import List
from sortedcontainers import SortedList
from collections import defaultdict


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # [movie] -> (available, rented)
        self.movies = defaultdict(lambda : (SortedList(), SortedList()))
        self.prices = {}
        self.all_movies_rented = SortedList()
        self.all_movies_available = set()
        
        for s, m, p in entries:
            self.movies[m][0].add((p, s))
            self.prices[(s, m)] = p
            self.all_movies_available.add((p, s, m))
        

    def search(self, movie: int) -> List[int]:
        available, _ = self.movies[movie]
        return [s for p, s in available[:5]]
        

    def rent(self, shop: int, movie: int) -> None:
        p = self.prices[(shop, movie)]
        self.movies[movie][0].remove((p, shop))
        self.movies[movie][1].add((p, shop))
        self.all_movies_available.remove((p, shop, movie))
        self.all_movies_rented.add((p, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        p = self.prices[(shop, movie)]
        self.movies[movie][1].remove((p, shop))
        self.movies[movie][0].add((p, shop))
        self.all_movies_rented.remove((p, shop, movie))
        self.all_movies_available.add((p, shop, movie))
        

    def report(self) -> List[List[int]]:
        return [[s,m] for (p, s, m) in self.all_movies_rented[:5]]
        
