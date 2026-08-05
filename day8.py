# There is a special case for creating single-item tuples. You must include a comma so Python knows it's a tuple and not regular parentheses:
# Tuples 
dog = ("Fido",)

# Because Tuples hold their data, multiple tuples can be stored within a list. Similar to storing other data in lists, each tuple within the list is separated by a comma. When accessing a list of tuples, the first index selects which tuple you want to access, the second selects a value within that tuple.


def get_heroes():
    heroes = [
        ("Glorfindel",
        2093,
        True) ,
        ("Gandalf",
        1054,
        False),
        ("Gimli",
        389,
        False),
        ("Aragorn",
        87,
        False),
    ]

    return heroes


run_cases = [
    (
        [
            (
                "Glorfindel",
                2093,
                True,
            ),
            (
                "Gandalf",
                1054,
                False,
            ),
            (
                "Gimli",
                389,
                False,
            ),
            (
                "Aragorn",
                87,
                False,
            ),
            
            
        ]
    ),
]

submit_cases = run_cases


def test(expected_output):
    print("---------------------------------")
    passed = True
    result = get_heroes()
    if not isinstance(result, list):
        print("Expected result to be a list")
        return False

    for i, hero in enumerate(expected_output):
        print(f"Expected: {hero} at index {i}")
        if i >= len(result):
            print(f"Actual: None at index {i}")
            print("Fail")
            passed = False
            continue
        print(f"Actual: {result[i]} at index {i}")
        if hero != result[i]:
            print("Fail")
            passed = False
        else:
            print("Pass")
    return passed


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

# Q2 reversing using range function 

def reverse_list(items):
    reverse = []
    for i in range(len(items)-1,-1,-1):
        reverse.append(items[i])
    return reverse


run_cases = [
    (
        ["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"],
        ["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"],
    ),
    ([1, 2, 300, 4, 5], [5, 4, 300, 2, 1]),
]

submit_cases = run_cases + [
    ([], []),
    (["a"], ["a"]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (
        ["apple", "banana", "cherry", "date", "elderberry"],
        ["elderberry", "date", "cherry", "banana", "apple"],
    ),
    (["hello", "world"], ["world", "hello"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input list: {input}")
    print(f"Expected reversed list: {expected_output}")
    result = reverse_list(input)
    print(f"Actual reversed list: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

# Q3 We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns two new lists:

# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from each message at that particular index.




def get_even_and_odd_teams(players):
    even = players[0::2]
    odd = players[1::2]
    return even, odd
    
            



run_cases = [
    (
        [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ],
        (
            ["Harry", "Ron", "Fred", "Draco", "Cho", "Lee", "Lavender", "Anthony"],
            [
                "Hermione",
                "Ginny",
                "Neville",
                "Luna",
                "Gregory",
                "Michael",
                "Frank",
                "Allan",
            ],
        ),
    ),
    (["Mike", "Walter", "Skyler", "Tuco"], (["Mike", "Skyler"], ["Walter", "Tuco"])),
]

submit_cases = run_cases + [
    (["Alice", "Bob", "Charlie", "David"], (["Alice", "Charlie"], ["Bob", "David"])),
    ([], ([], [])),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = get_even_and_odd_teams(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

# notes 
# fruits = ["apple", "banana", "orange"]

# print(list(enumerate(fruits)))
# So enumerate() simply creates (index, value) pairs.