from main import FoodRatings


def test_1():
    input = [
        "FoodRatings",
        "highestRated",
        "highestRated",
        "changeRating",
        "highestRated",
        "changeRating",
        "highestRated",
    ]

    params = [
        [
            ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
            ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
            [9, 12, 8, 15, 14, 7],
        ],
        ["korean"],
        ["japanese"],
        ["sushi", 16],
        ["japanese"],
        ["ramen", 16],
        ["japanese"],
    ]

    output = [None, "kimchi", "ramen", None, "sushi", None, "ramen"]

    result = []

    for i, p in zip(input, params):
        if i == "FoodRatings":
            obj = FoodRatings(*p)
            result.append(None)
        elif i == "changeRating":
            result.append(obj.changeRating(*p))
        elif i == "highestRated":
            result.append(obj.highestRated(*p))

    assert result == output, f"calculated {result}, expected {output}"


def test_2():
    input = [
        "FoodRatings",
        "changeRating",
        "highestRated",
        "changeRating",
        "changeRating",
        "changeRating",
        "highestRated",
        "highestRated",
    ]
    params = [
        [
            ["emgqdbo", "jmvfxjohq", "qnvseohnoe", "yhptazyko", "ocqmvmwjq"],
            ["snaxol", "snaxol", "snaxol", "fajbervsj", "fajbervsj"],
            [2, 6, 18, 6, 5],
        ],
        ["qnvseohnoe", 11],
        ["fajbervsj"],
        ["emgqdbo", 3],
        ["jmvfxjohq", 9],
        ["emgqdbo", 14],
        ["fajbervsj"],
        ["snaxol"],
    ]

    expected = [None, None, "yhptazyko", None, None, None, "yhptazyko", "emgqdbo"]

    result = []

    for i, p in zip(input, params):
        if i == "FoodRatings":
            obj = FoodRatings(*p)
            result.append(None)
        elif i == "changeRating":
            result.append(obj.changeRating(*p))
        elif i == "highestRated":
            result.append(obj.highestRated(*p))

    assert result == expected, f"calculated {result}, expected {expected}"


if __name__ == "__main__":
    test_1()
    test_2()
