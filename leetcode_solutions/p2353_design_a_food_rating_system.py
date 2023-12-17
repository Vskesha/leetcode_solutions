from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fc = {}
        self.fr = {}
        self.hrc = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.fc[f] = c
            self.changeRating(f, r)

    def changeRating(self, food: str, newRating: int) -> None:
        self.fr[food] = newRating
        c = self.fc[food]
        heappush(self.hrc[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.fr[self.hrc[cuisine][0][1]] != - self.hrc[cuisine][0][0]:
            heappop(self.hrc[cuisine])
        return self.hrc[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
def test():
    null = None

    commands = ["FoodRatings",
                "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
    args = [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
             ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
             [9, 12, 8, 15, 14, 7]],
            ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
    output = [null, "kimchi", "ramen", null, "sushi", null, "ramen"]

    fr = FoodRatings(*args[0])
    for i in range(1, len(commands)):
        print(f'Test 1-{i}... ', end='')
        res = getattr(fr, commands[i])(*args[i])
        assert res == output[i]
        print('OK')

    commands = ["FoodRatings",
                "changeRating", "highestRated", "changeRating", "changeRating",
                "changeRating", "highestRated", "highestRated"]
    args = [[["emgqdbo", "jmvfxjohq", "qnvseohnoe", "yhptazyko", "ocqmvmwjq"],
             ["snaxol", "snaxol", "snaxol", "fajbervsj", "fajbervsj"],
             [2, 6, 18, 6, 5]],
            ["qnvseohnoe", 11], ["fajbervsj"], ["emgqdbo", 3], ["jmvfxjohq", 9],
            ["emgqdbo", 14], ["fajbervsj"], ["snaxol"]]
    output = [null, null, "yhptazyko", null, null, null, "yhptazyko", "emgqdbo"]

    fr = FoodRatings(*args[0])
    for i in range(1, len(commands)):
        print(f'Test 2-{i}... ', end='')
        res = getattr(fr, commands[i])(*args[i])
        assert res == output[i]
        print('OK')


if __name__ == '__main__':
    test()
