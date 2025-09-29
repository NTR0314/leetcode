from typing import List
import heapq


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.heaps = {c: [] for c in set(cuisines)}
        self.cuisine_map = {f: c for f, c in zip(foods, cuisines)}
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_rating = {f: r for f, r in zip(foods, ratings)}
            heapq.heappush(self.heaps[c], (-r, f))
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        heapq.heappush(self.heaps[self.cuisine_map[food]], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        while self.heaps[cuisine]:
            potential_highest = self.heaps[cuisine][0]
            if potential_highest[0] == -self.food_to_rating[potential_highest[1]]:
                return potential_highest[1]
            else:
                heapq.heappop(self.heaps[cuisine])

        return ""
        